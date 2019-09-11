import sys
import os
from core.src import run
path = os.path.dirname(__file__)
sys.path.append(path)
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == '__main__':
    run()
