class Solution(object):
    '''
    Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.

    Clarifications:
        * function can be called with same node for inputs
        * a route will not always exist
        * nodes will exist in graph
        * graph will not be blank

    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    >>> path_exists(graph, 'A', 'B')
    True

    >>> path_exists(graph, 'A', 'A')
    True

    >>> path_exists(graph, 'E', 'A')
    False
    '''
    def path_exists(self, graph, start, end):
        if start == end:
            return True
        visited = [start]
        q = []
        q.extend(graph[start])
        while q != []:
            child = q.pop(0)
            if child == end:
                return True
            visited.extend(child)
            for grandchild in graph[child]:
                if grandchild not in visited and grandchild not in q:
                    q.extend(grandchild)
        return False


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}
sol = Solution()
print(sol.path_exists(graph, 'A', 'B'))
print(sol.path_exists(graph, 'A', 'A'))
print(sol.path_exists(graph, 'E', 'A'))
