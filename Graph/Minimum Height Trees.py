class Solution:
    # just remember
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
            
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remainNodeNum = n
        while remainNodeNum > 2:
            # delete leaves now and count new round
            remainNodeNum -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                # 将被删除的叶子节点的邻接节点的度减 1
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                # if degree ==1 then it is leaf
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            
            leaves = newLeaves

        return leaves