import logging
import sys
py_major_version = sys.version[0]
py2 = py_major_version == '2'

if py2:
    sys.exit("Python 2 is not supported.")

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)8s %(message)s')


from .numeric import number
from .filtered import filtered
from .grep import grep
from .undeletable import Undeletable
