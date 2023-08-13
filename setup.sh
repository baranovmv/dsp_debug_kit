#!/bin/bash

echo "py sys.path.insert(0, \"${PWD}/gdb_numpy\")" >> ~/.gdbinit
echo "py sys.path.insert(0, \"${PWD}/\")" >> ~/.gdbinit
echo "py import gdb_numpy as gdn" >> ~/.gdbinit
echo "py from spectrum import *" >> ~/.gdbinit
echo "py import matplotlib.pyplot as plt" >> ~/.gdbinit
