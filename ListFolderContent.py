import os
from tkinter import filedialog

tabs = 0
tabPath = ""
tabsmod = 0
tabsPlus = 0

rootDir = os.getcwd()
masterFilePath = os.path.join(rootDir, '__myList.txt')
with open(masterFilePath, 'w', encoding='utf-8') as f:
    for dirpaths, dirnames, filenames in os.walk(rootDir):
        _, root = os.path.split(dirpaths)
        if root == "":
            tabs = 0
        else:
            tabPath = dirpaths.replace('E:/', '')
            tabs = len(tabPath.split('\\'))
            tabsmod = tabs - 1
            tabsPlus = tabsmod + 1

        f.write('\n' + '\t' * tabsmod + root + '\n')

        if tabs == 0 and root == "":
            for file in filenames:
                f.write('\t' * tabs + file + '\n')
        else:
            for file in filenames:
                f.write('\t' * tabsPlus + file + '\n')

os.startfile(rootDir)