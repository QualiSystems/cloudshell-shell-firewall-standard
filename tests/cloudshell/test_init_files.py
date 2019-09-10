import os
import unittest

from gitignore_parser import parse_gitignore

from tests.cloudshell.base_test import PACKAGE_DIR


class TestInitFiles(unittest.TestCase):
    def test_init_has_extend_path(self):
        """Test that don't forget to extend path.

        It need to correct work import cloudshell packages
        """
        is_ignored_by_git = parse_gitignore(os.path.join(PACKAGE_DIR, ".gitignore"))
        for cur_dir, sub_dirs, files in os.walk(PACKAGE_DIR):

            for sub_dir in sub_dirs[:]:
                if is_ignored_by_git(os.path.join(PACKAGE_DIR, sub_dir)):
                    sub_dirs.remove(sub_dir)

            if "__init__.py" in files:
                path = os.path.join(cur_dir, "__init__.py")
                with open(path) as fo:
                    data = fo.read()

                self.assertIn(
                    "__path__ = extend_path(__path__, __name__)",
                    data,
                    "You have to add 'extend_path' in all __init__ files. "
                    "In {} missed".format(path),
                )
