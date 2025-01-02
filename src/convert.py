# This file defines the converter of the g01 to dat file type
import os
from g01 import CrossSection

class G01toDAT:
    def __init__(self,dir,name_g01,name_dat):
        self.dir = dir
        self.name_g01 = name_g01
        self.name_dat = name_dat
        self.g01 = None
        self.dat = None
        self.crosssections = []
    
    def open_g01(self):
        self.g01 = open(os.path.join(os.path.join(self.dir, "g01"), 
        f"{self.name_g01}.g01"), "r")
    
    def read_g01(self):
        section = None
        readingSection = False
        for line in self.g01.readlines():
            if line[0:10] == "#Sta/Elev=":
                temp = line.split(' ')
                section = CrossSection(int(temp[1]))
                readingSection = True
            elif line[0:6] == "#Mann=":
                readingSection = False
                self.crosssections.append(section)
                section = None
            elif readingSection:
                coordinates = line.split()
                for c in range(0,len(coordinates),2):
                    section.coordinates.append([coordinates[c+1],coordinates[c]])
        for i in range(len(self.crosssections)):
            self.crosssections[i].cs_number = (len(self.crosssections)-i)
    
    def write_dat(self):
        self.dat = open(os.path.join(os.path.join(self.dir,"dat"), f"{self.name_dat}.dat"), "w") 
        self.crosssections.sort(key=lambda x:x.cs_number)
        self.dat.write("T1")
        for section in self.crosssections:
            self.dat.write(f"\nX1{section.cs_number:6}{section.num_coordinates:8}\n")
            column_count = 0
            for coordinate in section.coordinates:
                # First column only accurate up to tenths
                if column_count == 0:
                    self.dat.write("GR")
                    if '.' not in coordinate[0]:
                        self.dat.write(f"{coordinate[0]}.0 ")
                    else:
                        if coordinate[0][-2] == '.':
                            self.dat.write(f"{coordinate[0]:>6} ")
                        else:
                            self.dat.write(f"{coordinate[0][:-2]}0 ")
                # Other columns accuarte up to hundreths
                else:
                    if '.' not in coordinate[0]:
                        self.dat.write(f"{coordinate[0]:>3}.00 ")
                    else:
                        if coordinate[0][-2] == '.':
                            self.dat.write(f"{coordinate[0]:>2}0 ")
                        else:
                            self.dat.write(f"{coordinate[0]:>6} ")

                if '.' not in coordinate[1]:
                    self.dat.write(f"{coordinate[1]:>4}.00 ")
                else:
                    if coordinate[1][-2] == '.':
                        self.dat.write(f"{coordinate[1]:>6}0 ")
                    else:
                        self.dat.write(f"{coordinate[1]:>7} ")

                if column_count == 4:
                    self.dat.write("\n")
                column_count += 1
                column_count = column_count % 5
        self.dat.write("\nEJ\n\nER")

        self.dat.close()
            
            
