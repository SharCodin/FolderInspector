import os
from tkinter import filedialog

startFolder = filedialog.askdirectory()

for i in os.walk(startFolder):
    for x in i[2]:
        if 'Instrumental' in x:
            path = os.path.join(i[0], x)
            os.remove(path)
