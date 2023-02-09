#Chương trình setup
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win64' :
    base = 'Win64GUI'

setup(name='Setup_PDT', version='1.0', description='Binary Conversion', executables=[Executable('Tkinter_12.py', base=base)])






