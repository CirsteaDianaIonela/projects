import sys

from setuptools import setup

__version__ = "0.0.0"

setup(
   name="my-package",
   version=__version__,
   # And so on...
)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass
