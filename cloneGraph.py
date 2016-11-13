# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        done_map, prog_map = dict(), dict()
        head = UndirectedGraphNode(node.label)
        prog_map[node.label] = [node, head]
        while len(prog_map) > 0:
            l, rootitem = prog_map.popitem()
            origin, root = rootitem[0], rootitem[1]
            done_map[origin.label] = root
            for nb in origin.neighbors:
                if nb.label != root.label:
                    if nb.label not in done_map and nb.label not in prog_map:
                        newnode = UndirectedGraphNode(nb.label)
                        prog_map[nb.label] = [nb, newnode]
                        root.neighbors.append(newnode)
                    elif nb.label in done_map:
                        root.neighbors.append(done_map[nb.label])
                    elif nb.label in prog_map:
                        root.neighbors.append(prog_map[nb.label][1])
                else:
                    root.neighbors.append(root)
        return head





