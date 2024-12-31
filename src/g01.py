# This file defines the storage method for each cross section of the g01 file

class CrossSection():
    def __init__(self, num_coordiantes):
        self.cs_number = None
        self.num_coordinates = num_coordiantes
        self.coordinates = []