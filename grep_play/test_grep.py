import os
import unittest
from contextlib import contextmanager

import sys

from grep_play.playwithgrep import run_job


class TestGrep(unittest.TestCase):

    def test_file_arg_and_empty_regex(self):
        CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
        test_file = '{}/tested_file.txt'.format(CONFIG_PATH)

        sys.argv = ['', '-e', '', test_file]
        with open(test_file, 'r') as f:
            ex_output = f.read()

        with capture_output() as (out, err):
            run_job()
        rl_output = out.getvalue().strip()
        assert rl_output == ex_output

    def test_file_arg_and_regex_all_as(self):
        CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
        test_file = '{}/tested_file.txt'.format(CONFIG_PATH)

        sys.argv = ['', '-e', 'as', test_file]
        ex_output = '''Nulla fringilla massa diam, molestie bibendum tellus interdum nec.
Maecenas bibendum ligula id scelerisque iaculis.
Cras mollis risus pellentesque tellus dignissim malesuada.
Duis eget gravida velit. Mauris bibendum massa vitae eros cursus, sed auctor dui elementum.
Cras tristique, eros eu egestas ullamcorper, elit nisi pulvinar dui, quis placerat lectus purus a justo.
Nunc sollicitudin, orci vel tincidunt elementum, massa dolor efficitur arcu, a scelerisque nulla mauris sit amet neque.'''

        with capture_output() as (out, err):
            run_job()
        rl_output = out.getvalue().strip()
        assert rl_output == ex_output

    def test_file_arg_and_regex_all_as_inverted(self):
        CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
        test_file = '{}/tested_file.txt'.format(CONFIG_PATH)

        sys.argv = ['', '-e', 'as', '-v', test_file]
        ex_output = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla nec laoreet magna.
Suspendisse posuere mauris at mi tempus pharetra.
Sed feugiat, orci non fringilla ultrices, urna est lobortis tortor, a aliquet lectus nunc in ex.
Mauris id arcu efficitur, scelerisque risus at, ullamcorper ante.
Nunc a orci sit amet libero eleifend commodo.'''

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