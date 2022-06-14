import __displaytable__
import numpy
from rich import print

reader = numpy.loadtxt(open("test1.csv", "rb"), delimiter=",", skiprows=1)
x = list(reader)
result = numpy.array(x).astype("float")

for i in result:
  print(i)

#create this as a display program and import it to main // show answer after this func is over ++ shift the logic to convert sop and pos here