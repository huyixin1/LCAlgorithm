class Solution:
    def __init__(self):
        self.all_path = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        on_path = []
        self.traverse(graph, 0, on_path)
        return self.all_path

    def traverse(self, graph: List[List[int]], s, on_path):
        # preposition, when graph has cycle it is to judge if it is on cycle path
        on_path.append(s)
        # end case
        length = len(graph)
        if s == length-1:
            self.all_path.append(list(on_path)) # needs to make a copy
            on_path.pop() # revoke the last node, next find other path
            return

        # base case
        for neighbor in graph[s]:
            self.traverse(graph, neighbor, on_path)
        # postposition
        on_path.pop()