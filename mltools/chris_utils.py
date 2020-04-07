################################################################################
## IMPORTS #####################################################################
################################################################################


import numpy as np
import matplotlib.pyplot as plt
import os

# This is meant to be a function to save a graph
def save_image(name, folder="Figures"):
    if not os.path.isdir(folder):
        os.makedirs(folder, 0o502, exist_ok=True)
        # Some operating systems ignore the mode in the makedirs function
        os.chmod(folder, 0o502)
        print("Test2")
        print("Path: \'", folder, "\' did not exist.")
    else:
        print("Path existed")


################################################################################
################################################################################
################################################################################
