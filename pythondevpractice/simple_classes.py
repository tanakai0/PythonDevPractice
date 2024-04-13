import logging

from pythondevpractice import simple_functions

logger = logging.getLogger(__name__)


class Human:
    def __init__(self, name: str, years: int, height: float) -> None:
        self.name = name
        self.years = years
        self.height = height
        logger.info("Human instance is successfully generated.")

    def print_info(self):
        """
        Introduce self

        Examples
        --------
        >>> h = Human("Bob", 19, 180)
        >>> h.print_info()
        Bob, 19 years-old, 180 cm
        """
        print(f"{self.name}, {self.years} years-old, {self.height} cm")

    def gets_older(self, year: int):
        logger.debug(f"year = {year}.")
        self.years = simple_functions.plus(self.years, year)


if __name__ == "__main__":
    h = Human("Bob", 19, 180)
    h.gets_older(10)
    h.print_info()
