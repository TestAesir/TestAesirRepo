from snap import *
from heapq import *

G = LoadEdgeList(PNGraph, "wiki-Vote.txt", 0, 1)

# Q1-1
nodeCount = G.GetNodes()
print '[Q1-1] The number of nodes in the network:', nodeCount
# print G.GetEdges()

# Q1-2
selfEdgeCount = CntSelfEdges(G)
print '[Q1-2] The number of nodes with a self-edge:', selfEdgeCount

# Q1-3
directedEdgeCount = CntUniqDirEdges(G)
print '[Q1-3] The number of directed edges in the network:', directedEdgeCount

# Q1-4
unDirectedEdgeCount = CntUniqUndirEdges(G)
print '[Q1-4] The number of undirected edges in the network:', unDirectedEdgeCount

# Q1-5
reciprocatedEdgeCount = CntUniqBiDirEdges(G)
print '[Q1-5] The number of reciprocated edges in the network:', reciprocatedEdgeCount

# Q1-6
outDegToCntV = TIntPrV()
GetOutDegCnt(G, outDegToCntV)
zeroOutDegreeNodes = outDegToCntV[0].GetVal2()
print '[Q1-6] The number of nodes of zero out-degree:', zeroOutDegreeNodes

# Q1-7
inDegToCntV = TIntPrV()
GetInDegCnt(G, inDegToCntV)
zeroinDegreeNodes = inDegToCntV[0].GetVal2()
print '[Q1-7] The number of nodes of zero in-degree:', zeroinDegreeNodes

# Q1-8
edgeOutOver10 = 0
for i in range(11, len(outDegToCntV)):
  edgeOutOver10 += outDegToCntV[i].GetVal2()
print '[Q1-8] The number of nodes with more than 10 outgoing edges (out-degree > 10):', edgeOutOver10

# Q1-9
edgeInFewer10 = 0
for i in range(0, 10):
  edgeInFewer10 += inDegToCntV[i].GetVal2()
print '[Q1-9] The number of nodes with fewer than 10 incoming edges (in-degree < 10):', edgeInFewer10
