_author__ = 'Made by Jurijus Pacalovas'
print(_author__)
import os
import shutil
os.system('Portal8.reg')
newpath = r'C:\Users\Public\Documents\Portal8' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
shutil.copyfile('Portal8.ico', 'C:\\Users\\Public\\Documents\\Portal8\\Portal8.ico')
shutil.copyfile('Portal8.py', 'C:\\Users\\Public\\Documents\\Portal8\\Portal8.py')
shutil.copyfile('Portal8_Start.py', 'C:\\Users\\Public\\Documents\\Portal8\\Portal8_Start.py')
os.system('Portal8_Start.py')
