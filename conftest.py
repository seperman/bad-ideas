import os
import sys

# Add the test path to Pythonpath to enable imports of Flex modules
the_path = os.path.dirname(__file__)

sys.path.append(os.path.dirname(the_path))


def pytest_addoption(parser):
    """Add additional options to the command line parser."""
    group = parser.getgroup('bad-ideas')

    group._addoption('--run-integration', action='store_true', default=False,
                     help='Run the slower, integration-style tests too.')
