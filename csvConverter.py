import os

if __name__ == '__main__':

    #filename change location
    filename = 'E:/Ajay RCC04 data/Final feb 22/slammer24_example_out.txt';

    #converted file location
    f2Filename = 'csvconvertedFile22.csv'
    
    if os.path.exists(f2Filename):
        os.remove(f2Filename)
    f2 = open(f2Filename, "a")
    
    with open(filename,'r') as f:
        line = f.readline();
        while line:
            lineStrip = line.replace(' ', ',');
            f2.write(lineStrip);
            line = f.readline();
    f.close();
    f2.close();
 
