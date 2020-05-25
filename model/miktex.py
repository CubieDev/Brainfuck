from os import environ, path
from sys import platform
import os, subprocess, pathlib

class MikTexNotFound(Exception):
    pass

class DirectoryNotFound(Exception):
    pass

class OSNotSupported(Exception):
    pass

class MikTex():
    """Statically processes all variables required to spawn a child process for miktex"""

    _engine = "pdflatex"
    _path = environ['PATH'].split(';')
    _exec = "{0}{1}".format(_engine,".exe") if ("win" in platform) else (_engine if ("linux" in platform) else "")
    mikTexPath = r""
    if(len(_exec) == 0):
        raise OSNotSupported("Interpreter only supports Windows and Linux platforms")

    mikTexPaths = [path.normpath(p) for p in _path if "miktex" in p.lower()]
    root = pathlib.Path(__file__).parent.absolute().parent.absolute()
    wdir = os.path.join(root, "Userfiles")

    #TODO: Potentially allow user to pick miktex installation
    if (len(mikTexPaths) >= 1):
        mikTexPath = os.path.join(mikTexPaths[0], _exec)
        if not os.path.exists(mikTexPath):
            raise MikTexNotFound(f"No tex to pdf processor found in MikTex folder: {mikTexPath}")
    else:
        raise MikTexNotFound("No MikTex installation found in PATH")

    if not os.path.exists(wdir):
        raise DirectoryNotFound(f"Directory {wdir} could not be located")

    # mikTexThread = subprocess.Popen([_engine, "test.tex"], cwd=wdir)
    # mikTexThread.wait()
# print(wdir)

