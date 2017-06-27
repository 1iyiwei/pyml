import os, theano

total_path = os.path.join(os.path.dirname(theano.__file__), "misc", "check_blas.py")

os.system("python " + total_path)
