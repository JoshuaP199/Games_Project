@echo off
::Delete all gui.tut files EXCEPT for the py file and delete the build and cache folders

::change path to where it is on your pc
cd C:\Users\joshp\OneDrive\Desktop\test
pyinstaller --onefile gui_tut.py

pause