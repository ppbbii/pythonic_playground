import unittest
from contextlib import contextmanager

import sys

from cut_play.playwithcut import run_job


class TestCut(unittest.TestCase):
    def test_version_expected_output(self):
        expected_output = 'VER 0.1'

        # given
        sys.argv = ['', '-v']

        # when
        with capture_output() as (out, err):
            run_job()

        # then
        assert out is not None
        rl_output = out.getvalue().strip()
        assert rl_output == expected_output

    def test_character_cut(self):
        expected_output = '1\n1\n1\n1\n1'

        # given
        sys.argv = ['', '-c', '1', 'test.txt']

        # then
        with capture_output() as (out, err):
            run_job()

        # then
        assert out is not None
        rl_output = out.getvalue().strip()
        assert rl_output == expected_output

    def test_character_cut_range(self):
        expected_output = '1\n1\n1\n1\n1'

        # given
        sys.argv = ['', '-c', '1-3', 'test.txt']

        # then
        with capture_output() as (out, err):
            run_job()

        # then
        assert out is not None
        rl_output = out.getvalue().strip()
        assert rl_output == expected_output


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