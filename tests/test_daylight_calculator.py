import os
import sys

import pytest

from daylight_calculator import DaylightCalculator

src_path = os.path.abspath(os.path.join(os.getcwd(), "src"))
sys.path.append(src_path)


def test_nautical_exposure():
    # TODO: Implement a test for nautical_exposure method
    pass


def test_realistic_daylight():
    DC_Instance = DaylightCalculator(location="TestLocation", orography="TestOrography")
    DC_Instance.realistic_daylight()

    assert True


if __name__ == "__main__":
    test_realistic_daylight()
