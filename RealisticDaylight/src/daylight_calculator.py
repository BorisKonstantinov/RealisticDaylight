""" This module contains the DaylightCalculator class."""

class DaylightCalculator:
    """ Deals with handling calculations for daylight exposure.
    """
    def __init__(self, location, orography):
        self.location = location
        self.orography = orography

    def nautical_exposure(self):
        """ Returns the nautical sunrise and sunset times.
        """
        # Issue #7: Write function calculating nautical day length

    def realistic_daylight(self):
        """ Returns the sunrise and sunset times with orography factored in.
        """
        # Issue #8: Write function calculating true day length
        print("Hello World from DaylightCalculator.realistic_daylight()")
