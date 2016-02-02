# For pathname munging
import os
import subprocess

# The module that build_tests comes from.
from gabbi import driver

import ofcourse.util

ofcourse.util.base_dir = '/tmp/ofcourse-tests'

from ofcourse.site import app  # noqa PEP8 ignore

try:
    subprocess.check_output(['rm', '-rf', '/tmp/ofcourse-tests'])
except:
    pass

os.mkdir('/tmp/ofcourse-tests')
subprocess.check_call(['ofcourse', 'new'], cwd='/tmp/ofcourse-tests')


# By convention the YAML files are put in a directory named
# "gabbits" that is in the same directory as the Python test file.
TESTS_DIR = 'gabbits'


def get_app():
    return app


def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process."""
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    return driver.build_tests(test_dir, loader,
                              intercept=get_app)
