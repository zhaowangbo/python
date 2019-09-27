import os
import sys
from core import src

path = os.path.dirname(__file__)
sys.path.append(path)
print(sys.path)

if __name__ == "__main__":
    src.run()

