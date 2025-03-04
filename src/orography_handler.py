import pandas as pd


class OrographyHandler:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def get_orography_data(self, location):
        # TODO
        # Process and return orography data.
        # This function returns the angle to the top of the
        # orographical obstacle in line with the solar path
        # on that day, for that location.
        pass
