import sys
import os

path = os.path.dirname(__file__)
sys.path.append(path)
print(sys.path)
from core import src

if __name__ == '__main__':
    src.run()
