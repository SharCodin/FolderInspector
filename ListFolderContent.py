import os
from tkinter import filedialog

rootDir = filedialog.askdirectory()
masterFilePath = os.path.join(rootDir, '__myList.txt')
with open(masterFilePath, 'w', encoding='utf-8') as f:
    for dirpaths, dirnames, filenames in os.walk(rootDir):
        _, root = os.path.split(dirpaths)
        f.write(root + '\n\t')
        for file in filenames:
            f.write(file + '\n\t')
        for dirname in dirnames:
            f.write(dirname + '\n\t')
        f.write('\n')