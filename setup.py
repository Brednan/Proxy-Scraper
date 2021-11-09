import sys
from cx_Freeze import Executable, setup

setup(
    name='Proxy Scraper',
    version=1,
    description='A bot that goes through a few sites that contain proxy lists and scrapes them',
    executables = [Executable('GUI.py', base='Win32GUI')]
)