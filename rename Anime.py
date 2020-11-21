import os
from tkinter import filedialog
import re

root_directory = filedialog.askdirectory()

string_start_reg = re.compile(r'.*(EP.|ep.|Ep.|eP.)')
string_end_reg = re.compile(r'(.360p|.480p|.720p)')

for dirpaths, _, filenames in os.walk(root_directory):
	for file_name in filenames:
		if "EP." in file_name:
			old_file = os.path.join(dirpaths, file_name)
			_, directory = os.path.split(dirpaths)
			reg_start = re.sub(string_start_reg, directory + ' - Episode ', file_name)
			final_name = re.sub(string_end_reg, '', reg_start)
			checking = final_name.split('Episode ')[-1].split('.')[0]
			if float(checking) < 10:
				padding = '00'
			elif float(checking) < 100:
				padding = '0'
			else:
				padding = ''
			renamed = final_name.replace('Episode ', 'Episode ' + padding)
			new_file = os.path.join(dirpaths, renamed)
			os.rename(old_file, new_file)
