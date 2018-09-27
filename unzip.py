# decompression des d'offres
import os,glob

def unzip(path = 'path to archives'):

    #move to directory that containes archives
    os.chdir(path)
    f = open("names.txt", "a")
    #decoumpresse files
    for filename in os.listdir(path):
        name = str(filename)
        x = len(name)
        directory = name[:(x-4)]
        if not str("\""+directory+"\" ") in open('names.txt').read() and name.endswith('.zip'):
            os.system("unzip -o \""+name+"\" -d \""+directory+"\"")
    
    
    #creat file of dirnames sorted by last update
    files = glob.glob("*.zip")
    files.sort(key=os.path.getmtime)
    f = open("names.txt", "a")
    for file in files:
        if not str("\""+file+"\" ") in open('names.txt').read():
            x = len(file)
            f.write("\""+file[:(x-4)]+"\" ")
