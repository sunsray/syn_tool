#!/usr/bin/env python
# coding=utf-8

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

packages = [
    'os'

]

options = {
    'build_exe': {'packages': packages, 'icon': 'caterpillar_machine_72.ico',"include_files": ["func_click.pkl"],
                  "includes": ["atexit"]}
}

executables = [Executable('main_app.py', base=base, targetName='syntool.exe', shortcutName="SynTool",
                          shortcutDir='DesktopFolder')]

setup(
    name="SynItool",
    version="1.0.0",
    url='http://future.dreams.edu.cn/',
    author='liuguanghui',
    author_email='sunsray@163.com',
    description="it service",
    options=options,
    executables=executables
)
