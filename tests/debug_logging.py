import logging

from pythondevpractice.simple_classes import Human
from pythondevpractice.simple_functions import minus, plus


def set_logging():
    logging.basicConfig()
    package_name = "pythondevpractice"
    module_levels = {package_name + ".simple_classes": logging.INFO, package_name + ".simple_functions": logging.DEBUG}
    for module, level in module_levels.items():
        logging.getLogger(module).setLevel(level=level)


if __name__ == "__main__":
    set_logging()
    c = plus(10, 90)
    d = minus(0, 22)
    e = Human("May", 22, 160)
