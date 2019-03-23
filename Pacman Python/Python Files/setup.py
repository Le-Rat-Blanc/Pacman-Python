from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\155\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\155\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6'
setup(
    name = "Pacman Python",
    version = "1.0",
    author = "Benhamza Romain",
    author_email = "atchoumgefomi@gmail.com",
    options = {"build_exe": {"packages":["pygame"],
                         "include_files": ["win.png","lose.png"]}},
    executables = [Executable("Pacman Python.py",icon="pacman.ico")],
    )