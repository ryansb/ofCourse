import subprocess
import shutil
import tempfile
import unittest


class TestOfcourseNew(unittest.TestCase):
    def test_new(self):
        dir = tempfile.mkdtemp('ofcoursetest')
        subprocess.check_call(['ofcourse', 'new'], cwd=dir)
        shutil.rmtree(dir)
