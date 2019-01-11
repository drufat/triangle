import contextlib
import os
import textwrap
from pathlib import Path

import jinja2
import matplotlib as mplt
import matplotlib.pyplot as plt
import pygments as pyg
from docutils.parsers.rst import directives, Directive

__version__ = 3

mplt.use("Agg")
os.environ.pop('DISPLAY')


def get_text(name):
    d = Path(__file__).parent
    return (d / name).read_text()


templates = {
    name: jinja2.Template(get_text(f'{name}.jinja2'))
    for name in ('plot', 'code')
}


def setup(app):
    app.add_directive('plot', PlotDirective)

    default_pre_code = ''
    default_formats = [
        'png', 'hires.png', 'pdf'
    ]

    app.add_config_value('plot_pre_code', default_pre_code, True)
    app.add_config_value('plot_include_source', False, True)
    app.add_config_value('plot_html_show_source_link', True, True)
    app.add_config_value('plot_formats', default_formats, True)
    app.add_config_value('plot_basedir', None, True)
    app.add_config_value('plot_html_show_formats', True, True)
    app.add_config_value('plot_working_directory', None, True)
    app.add_config_value('plot_build_directory', None, True)

    app.connect('doctree-read', mark_plot_labels)

    return {
        'version': f'{__version__}',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def _option_boolean(arg):
    if not arg or not arg.strip():
        # no argument given, assume used as a flag
        return True
    elif arg.strip().lower() in ('no', '0', 'false'):
        return False
    elif arg.strip().lower() in ('yes', '1', 'true'):
        return True
    else:
        raise ValueError(f'"{arg}" unknown boolean')


def _option_format(arg):
    return directives.choice(arg, ('python', 'doctest'))


def _option_align(arg):
    return directives.choice(arg, (
        "top", "middle", "bottom",
        "left", "center", "right",
    ))


class PlotDirective(Directive):
    has_content = True
    required_argument = 0
    optional_arguments = 2
    final_argument_whitespace = False
    option_spec = {
        'alt': directives.unchanged,
        'height': directives.length_or_unitless,
        'width': directives.length_or_percentage_or_unitless,
        'scale': directives.nonnegative_int,
        'align': _option_align,
        'class': directives.class_option,
        'include-source': _option_boolean,
        'format': _option_format,
        'encoding': directives.encoding,
        'code': _option_boolean,
    }

    def run(self):
        document = self.state_machine.document
        env = document.settings.env
        app = env.app
        config = env.config

        self.options.setdefault('include-source', config.plot_include_source)
        self.options.setdefault('code', False)

        conf_dir = Path(app.confdir)
        src_dir = Path(app.builder.srcdir)

        rst_file = Path(document.attributes['source'])
        rst_dir = rst_file.parent
        if config.plot_working_directory:
            work_dir = Path(config.plot_working_directory)
        else:
            work_dir = rst_dir

        if len(self.arguments):
            src = directives.uri(self.arguments[0])
            if config.plot_basedir:
                src = conf_dir / config.plot_basedir / src
            else:
                src = src_dir / src
            code = src.read_text()
            caption = '\n'.join(self.content)
            name = Path(src.name)
        else:
            src = Path(rst_file)
            code = textwrap.dedent('\n'.join(self.content))
            counter = document.attributes.get('_plot_counter', 0) + 1
            document.attributes['_plot_counter'] = counter
            caption = ''
            name = Path('%s-%d.py' % (src.stem, counter))

        src_rel_dir = src.relative_to(conf_dir).parent

        build_dir = conf_dir / 'plot_build'
        if not build_dir.exists():
            build_dir.mkdir(parents=True)

        out_dir = build_dir / src_rel_dir
        if not out_dir.exists():
            out_dir.mkdir(parents=True)

        relpath = Path(os.path.relpath(out_dir, rst_dir))
        link = relpath / name.stem

        # write sources
        if config.plot_pre_code:
            code = config.plot_pre_code + '\n\n' + code

        (build_dir / src_rel_dir / name).write_text(code)

        # render code
        png = pyg.highlight(code, pyg.lexers.PythonLexer(), pyg.formatters.ImageFormatter(line_numbers=False))
        (build_dir / src_rel_dir / name.with_suffix('.py.png')).write_bytes(png)

        # render images
        img = ImageFile(name.stem, src_rel_dir, config.plot_formats)
        img.render(code, build_dir, work_dir)

        # generate output restructuredtext
        opts = [
            ':%s: %s' % (key, val) for key, val in self.options.items()
            if key in ('alt', 'height', 'width', 'scale', 'align', 'class')
        ]
        if self.options['code']:
            template = templates['code']
        else:
            template = templates['plot']

        result = template.render(
            link=link,
            options=opts,
            formats=img.formats,
            include_source=self.options['include-source'],
            html_show_formats=config.plot_html_show_formats,
            caption=caption
        )

        self.state_machine.insert_input(result.split('\n'), source=str(src))

        errors = []
        return errors


@contextlib.contextmanager
def cwd(path):
    """
    Change current directory.
    """
    prev = Path.cwd()
    os.chdir(str(path))
    try:
        yield
    finally:
        os.chdir(str(prev))


def mark_plot_labels(app, doctree):
    """
    To make plots referenceable, we need to move the reference from
    the "htmlonly" (or "latexonly") node to the actual figure node
    itself.
    """
    for name, explicit in doctree.nametypes.items():
        if not explicit:
            continue
        labelid = doctree.nameids[name]
        if labelid is None:
            continue
        node = doctree.ids[labelid]
        if node.tagname in ('html_only', 'latex_only'):
            for n in node:
                if n.tagname == 'figure':
                    sectname = name
                    for c in n:
                        if c.tagname == 'caption':
                            sectname = c.astext()
                            break

                    node['ids'].remove(labelid)
                    node['names'].remove(name)
                    n['ids'].append(labelid)
                    n['names'].append(name)
                    doctree.settings.env.labels[name] = (
                        doctree.settings.env.docname,
                        labelid,
                        sectname,
                    )
                    break


def parse_formats(plot_formats):
    def default_dpi(fmt):
        return {
            'hires.png': 200,
            'pdf': 200,
        }.get(fmt, 80)

    def get(fmt):

        if isinstance(fmt, str):
            if ':' in fmt:
                return get(fmt.split(':'))
            return fmt, default_dpi(fmt)

        if isinstance(fmt, (tuple, list)) and len(fmt) == 2:
            return str(fmt[0]), int(fmt[1])

        raise RuntimeError('invalid image format "%r" in plot_formats' % fmt)

    return [get(_) for _ in plot_formats]


class ImageFile:

    def __init__(self, stem, parent, formats):
        self.stem = stem
        self.parent = parent

        fmt_dpi = parse_formats(formats)
        self.formats = [fmt for fmt, dpi in fmt_dpi]
        self.dpi = {fmt: dpi for fmt, dpi in fmt_dpi}

    def path(self, format):
        return Path(self.parent) / f'{self.stem}.{format}'

    def paths(self):
        return [self.path(fmt) for fmt in self.formats]

    def render(self, code, build_dir, work_dir):
        plt.close('all')

        with cwd(work_dir):
            ns = {}
            exec(code, ns)

        for fmt in self.formats:
            plt.savefig(build_dir / self.path(fmt), dpi=self.dpi[fmt])

        plt.close('all')

        return ns
