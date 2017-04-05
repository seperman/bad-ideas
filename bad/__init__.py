import logging


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)8s %(message)s')


from .numeric import number
from .filtered import filtered
from .grep import grep
from .undeletable import Undeletable
