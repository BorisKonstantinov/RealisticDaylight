from .daylight_calculator import DaylightCalculator
from .orography_handler import OrographyHandler


def main():
    data_path = "path/to/orography_data.csv"
    location = "some_location"

    daylight_calculator = DaylightCalculator(location, orography_data)
    nautical_times = daylight_calculator.nautical_exposure()
    realistic_times = daylight_calculator.realistic_daylight()

    orography_handler = OrographyHandler(data_path)
    orography_data = orography_handler.get_orography_data(location)

    print(f"Nautical Sunrise and Sunset: {nautical_times}")
    print(f"Realistic Sunrise and Sunset: {realistic_times}")


if __name__ == "__main__":
    main()
