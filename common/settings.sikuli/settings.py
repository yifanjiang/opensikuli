import sys, os, inspect

# add common directory to import path
# COMMONPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + os.sep + ".."
# LIBPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + os.sep + ".."
# if not COMMONPATH in sys.path: sys.path.append(COMMONPATH)
# add test cases directory to import path

# test data root path
TESTDATAPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + os.sep + ".." + os.sep + "testdata"
