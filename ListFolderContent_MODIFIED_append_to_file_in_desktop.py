import os
import ctypes
import pyperclip

pyperclip.copy('Err')
tabs = 0
tabPath = ""
tabsmod = 0
tabsPlus = 0
rootDir = "D:/"
saveFile = r"C:\Users\Sharvin\Desktop"
masterFilePath = os.path.join(saveFile, '__myList.txt')
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

        if tabsmod == 0:
            f.write('\n')

        f.write('\t' * tabsmod + root + '\n')

        if tabs == 0 and root == "":
            for file in filenames:
                f.write('\t' * tabs + file + '\n')
        else:
            for file in filenames:
                f.write('\t' * tabsPlus + file + '\n')

with open(masterFilePath, 'r', encoding='utf-8') as f:
    copiedText = f.read()
    pyperclip.copy(copiedText)

print('='.center(40, '='))
print('COMPLETED'.center(40, '='))
print('='.center(40, '='))