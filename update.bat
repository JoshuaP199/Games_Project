@echo off
::Delete all gui.tut files EXCEPT for the py file and delete the build and cache folders

pip install pyinstaller

::change path to where it is on your pc
cd C:\Users\joshp\OneDrive\Documents\GitHub\Games_Project
pyinstaller --onefile gui_tut.py

pause