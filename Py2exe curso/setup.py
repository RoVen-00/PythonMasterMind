from distutils.core import setup
import py2exe
import os
import sqlite3
from time import sleep
from random import randrange
from pathlib import Path
import re
import glob

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      windows=["H4X0RRSCRIPT.py"])
