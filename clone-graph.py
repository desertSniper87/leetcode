"""
# Definition for a Node.

"""

# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = []

class Solution:

    def getNode(self, val, nodes) -> 'Node':


        if not nodes.get(val):

            nodes[val] = Node(val=val, neighbors=[])
    
        
        return nodes[val]

    def cloneGraph(self, node: 'Node', nodes=None) -> 'Node':
        if not nodes:
            nodes = {}
        
        if not node:
            return node



        returnNode = self.getNode(node.val, nodes)


        if node.neighbors:
            for n in node.neighbors:
                returnNode.neighbors.append(nodes.get(n.val) if nodes.get(n.val) else self.cloneGraph(n, nodes))


        for i in returnNode.neighbors:
            print(i.val)



        return returnNode
