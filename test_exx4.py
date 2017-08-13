import unittest
from contextlib import contextmanager
from unittest.mock  import MagicMock

import sys

from exx4 import parse_sysargv_to_list_of_dicts


class TestExx4(unittest.TestCase):
    def test_expected_output(self):
        sys.argv = MagicMock(return_value=['f1', 'f2', 'f3', '-o', 'a1', '-o', 'a2', '-o', 'a3'])
        with capture_output() as (out, err):
            parse_sysargv_to_list_of_dicts()
            print('bla {}'.format(out))
            assert out is not None

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