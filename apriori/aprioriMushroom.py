
# aprioriMushroom.py

import apriori
from numpy import *

mushRoomDataSet = [line.split() for line in open('mushroom.dat').readlines()]
L, supportData = apriori.apriori(mushRoomDataSet, minSupport = 0.3)

print 'find target in dual set : '
for item in L[1]:
	if item.intersection('2'):
		print item

print 'find target in qual set : '
for item in L[3]:
	if item.intersection('2'):
		print item



























