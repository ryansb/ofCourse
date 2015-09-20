"""
Author: Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
        Sam Lucidi <mansam@csh.rit.edu>
License: Apache 2.0

"""

import os

# flask dependencies
import flask
import flask.ext.mako as mako
from jinja2 import TemplateNotFound
from mako.exceptions import TopLevelLookupException

# ofcourse dependencies
from .util import app_path


def render_init(app):
    ' Wrap initialization for Mako templates '
    mako.MakoTemplates(app)
    app.config['MAKO_TRANSLATE_EXCEPTIONS'] = False


def render_template(template, **kwargs_raw):
    '''
    Try several template render methods

    Default to Jinja2 templates, fallback to mako
    '''
    templates = [
        (flask.render_template, ".html", {}, TemplateNotFound),
        (mako.render_template, ".mak",
            {'name': 'mako'}, TopLevelLookupException),
    ]
    for render, suff, keys, ex in templates:
        try:
            kwargs = kwargs_raw.copy()
            kwargs.update(keys)
            return render(template + suff, **kwargs)
        except ex:
            pass
