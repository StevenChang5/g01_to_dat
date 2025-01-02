import os
import sys
from convert import G01toDAT

def main():
    path = os.getcwd()
    print(os.path.join(path,"g01"))
    for filename in os.listdir(os.path.join(path,"g01")):
        if filename.endswith('.g01'):
            print(filename[:-4])
            g2d = G01toDAT(path, filename[:-4], filename[:-4])
            g2d.open_g01()
            g2d.read_g01()
            g2d.write_dat()

if __name__ == "__main__":
    main()
