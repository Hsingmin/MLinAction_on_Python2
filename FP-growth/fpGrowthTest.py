
# fpGrowthTest.py

import fpGrowth
from numpy import *

'''
# FP-Tree node create test

rootNode = fpGrowth.treeNode('pyramid', 9, None)

rootNode.children['eye'] = fpGrowth.treeNode('eye', 13, None)

rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix', 3, None)

rootNode.disp()
'''

simData = fpGrowth.loadSimpleData()
print('simData : ' , simData)

initSet = fpGrowth.createInitSet(simData)
print('initSet : ', initSet)

simFPTree, simHeaderTable = fpGrowth.createTree(initSet, 3)

simFPTree.disp()

freqItems = []
fpGrowth.mineTree(simFPTree, simHeaderTable, 3, set([]), freqItems)

print '============ news clicks digging  =========== '

parseData = [line.split() for line in open('kosarak.dat').readlines()]
initSet = fpGrowth.createInitSet(parseData)
newFPTree, newFPHeaderTable = fpGrowth.createTree(initSet, 100000)

newFreqList = []
fpGrowth.mineTree(newFPTree, newFPHeaderTable, 100000, set([]), newFreqList)
print 'len(newFreqList = )', len(newFreqList)
print '--------- newFreqList --------'
print newFreqList






















