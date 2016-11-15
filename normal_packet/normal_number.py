import random
import sys

mean=float(sys.argv[1])

standard_dev=float(sys.argv[2])


n=random.gauss(mean,standard_dev)
while(n < 0) :
	n=random.gauss(mean,standard_dev)

print "%.6f" % n +'M'



