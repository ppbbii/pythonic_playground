import os
import unittest
from contextlib import contextmanager

import sys

from grep_play.playwithgrep import run_job


class TestGrep(unittest.TestCase):

    def test_file_arg(self):
        CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
        test_file = '{}/tested_file.txt'.format(CONFIG_PATH)

        sys.argv = ['', '-e', '', test_file]
        with open(test_file, 'r') as f:
            ex_output = f.read()

        with capture_output() as (out, err):
            run_job()
        rl_output = out.getvalue().strip()
        assert rl_output == ex_output

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