import multiprocessing
import sys

print("Python version: {version}".format(version=sys.version))
print("Total cores: {cores}".format(cores=multiprocessing.cpu_count()))


if True:
  print("This will be covered")
else:
  print("This will NOT be covered and may contain some errors")
  print("For example division by zero")
  a = 1
  b = 0
  c = a / b
