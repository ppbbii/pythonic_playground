import os
import unittest
from contextlib import contextmanager

import sys

from src.find_play.findfind import run_job

class TestFind(unittest.TestCase):
    def test_expected_output(self):
        CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
        sys.argv = ['', CONFIG_PATH, '-n', '\w+']
        ex_output = '''{0}/test_find.py\n{1}/findfind.py'''\
            .format(CONFIG_PATH, CONFIG_PATH)
        ex_output_v2 = '''{0}/findfind.py\n{1}/test_find.py''' \
            .format(CONFIG_PATH, CONFIG_PATH)

        with capture_output() as (out, err):

            run_job()

        assert out is not None
        rl_output = out.getvalue().strip()
        assert (rl_output == ex_output or
            rl_output == ex_output_v2)

@contextmanager
def capture_output():
    from io import StringIO
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err