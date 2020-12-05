import os
from tkinter import filedialog
from timeit import default_timer as Timer
from datetime import timedelta

startTimer = Timer()

blacklisted = ['gnirehtet-rust-win64-v2.4', '.vscode', 'venv']

tabs = 0
tabPath = ""
tabsmod = 0
tabsPlus = 0

rootDir = os.getcwd()
initial_tabs = len(rootDir.split('\\'))
masterFilePath = os.path.join(rootDir, '__myList.txt')
with open(masterFilePath, 'w', encoding='utf-8') as f:
    for dirpaths, dirnames, filenames in os.walk(rootDir):
        skipped = False
        for blacklisted_item in blacklisted:
            if blacklisted_item in dirpaths:
                skipped = True
                break
        if skipped == True:
            continue
        _, root = os.path.split(dirpaths)
        current_tabs = len(dirpaths.split('\\'))
        tab_spaces_dir = current_tabs - initial_tabs
        tab_spaces_files = tab_spaces_dir + 1

        f.write('\t' * tab_spaces_dir + root + '\n')

        for file in filenames:
            if '__myList.txt' in file:
                continue
            f.write('\t' * tab_spaces_files + file + '\n')

        if len(filenames) > 0:
            f.write('\n')

stopTimer = Timer()
print((str(timedelta(seconds=(round(stopTimer - startTimer, 2))))).center(50, '='))
