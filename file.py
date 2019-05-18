import os
import sys
import glob


def searchWindows():
    route = 'c:\\'
    files = []
    posibleFiles = [".dll", ".exe", ".drv", ".ocx"]
    csvFile = open(os.getcwd()+"/file.csv", "w")
    csvFile.write("Nombre,Tamaño (bytes)\n")
    for posibleFile in posibleFiles:
        # set to True later para entrar dentro a la carpeta de carpetas
        for f in glob.glob(route+"**/*"+posibleFile, recursive=True):
            try:
                files.append(f)
                opened = open(f, "rb")
                dictionary = dict()
                print(opened)
                readedFile = opened.readlines()[2:]
                for line in readedFile:
                    for char in str(line).split("\\x"):
                        if(len(char) == 2):
                            if(char not in dictionary):
                                dictionary[char] = 1
                            else:
                                dictionary[char] = dictionary[char]+1
                size = os.path.getsize(f)
                csvFile.write(str(f.split("\\")[-1])+","+str(size)+"\n")
                for key, value in dictionary.items():
                    try:
                        checkHex = int(key, 16)
                        csvFile.write(str(key)+","+str(value)+"\n")
                    except:
                        pass
                        '''
                csvFile.write("\n")
                for key, value in dictionary.items():
                    try:
                        checkHex = int(key, 16)
                        csvFile.write(str(value)+",")
                    except:
                        pass
                csvFile.write("\n")
                '''
                opened.close()
            except:
                print("File probabbly not found")
    # Not completely necessary, but if u want to print which file is being readed here u have it.
    csvFile.close()

    return files, dictionary


# WindowsDictionary contains all pair of (Hex, TimesOnDocumentValues)
files, windowsDictionary = searchWindows()
# createCSV
# Headers
