
"""
The vivisect.parsers package contains all the known file format parsers
for vivisect.  Each parser module must implement the following functions:

    parseFile(workspace, filename):
        Load the file into the given workspace
    parseBytes(workspace, bytes):
        Load the file (pre-read in) into the workspace

"""
# Some parser utilities

import md5
import sys
import struct

import vstruct.defs.macho as vs_macho

from .utils import md5File
from .utils import md5Bytes
from .utils import guessFormat
from .utils import guessFormatFilename


def getParserModule(fmt):
    # wb: this importing by incomplete package doesn't seem like a
    #  good idea. but, this works with pyinstaller
    if fmt == "pe":
        import pe
        return pe
    elif fmt == "blob":
        import blob
        return blob
    elif fmt == "elf":
        import elf
        return elf
    elif fmt == "ihex":
        import ihex
        return ihex
    elif fmt == "macho":
        import macho
        return macho

    mname = "%s" % fmt
    mod = sys.modules.get(mname)
    if mod == None:
        __import__(mname)
        mod = sys.modules[mname]
    return mod

