"""
Author: Matt Soucy <msoucy@csh.rit.edu>
        Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
        Sam Lucidi <mansam@csh.rit.edu>
License: Apache 2.0

"""

from functools import partial

# flask dependencies
import flask


# Renderers {{{
# Renderer template {{{
def make_renderer(render, suffixes, exception,
                  init=None, config={}, params={}):
    class Renderer(object):
        def __init__(self, app):
            ''' Perform required setup '''
            if init:
                init(app)
            app.config.update(config)

        def __call__(self, template, **kwargs_raw):
            ''' Attempt to render '''
            kwargs = kwargs_raw.copy()
            kwargs.update(params)
            for suffix in suffixes:
                try:
                    return render(template + suffix, **kwargs)
                except exception:
                    pass
    return Renderer
# }}}

_renderer_classes = []

# Jinja2 files (.html) {{{
try:
    import jinja2
    _renderer_classes.append(make_renderer(
        flask.render_template, (".html", ".htm"), jinja2.TemplateNotFound))
except ImportError:
    # Somehow, jinja isn't supported
    pass
# }}}

# Mako files (.mak) {{{
try:
    import flask.ext.mako as mako
    from mako.exceptions import TopLevelLookupException
    _renderer_classes.append(make_renderer(
        mako.render_template, (".mak", ".mako"), TopLevelLookupException,
        init=mako.MakoTemplates,
        params={'name': 'mako'},
        config={'MAKO_TRANSLATE_EXCEPTIONS': False}))
except ImportError:
    # Mako extensions don't exist
    pass
# }}}
# }}}

# Filters {{{
_filters = []

# Markdown {{{
try:
    import markdown
    _filters.append(
        ("markdown", partial(markdown.markdown, extensions=("extra",))))
except:
    pass
# }}}

# reStructuredText {{{
try:
    from docutils.core import publish_parts
    _filters.append((
        "rst",
        lambda txt: publish_parts(txt, writer_name='html')['fragment']))
except:
    pass
# }}}
# }}}

_renderers = []


def render_init(app):
    '''
    Set up all renderers and filters for a provided class
    '''
    global _renderers
    _renderers = []
    for cls in _renderer_classes:
        _renderers.append(cls(app))
    for name, filt in _filters:
        app.jinja_env.filters[name] = filt


def render_template(template, **kwargs_raw):
    '''
    Try several template render methods

    Default to Jinja2 templates, fallback to mako
    '''
    for render in _renderers:
        ret = render(template, **kwargs_raw)
        if ret is not None:
            return ret

# vim: fdm=marker:et:ts=4:sw=4
