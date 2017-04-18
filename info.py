import multiprocessing
import sys

print("Python version: {version}".format(version=sys.version))
print("Total cores: {cores}".format(cores=multiprocessing.cpu_count()))
