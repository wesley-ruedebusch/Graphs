from util import Stack, Queue  

def earliest_ancestor(ancestors, starting_node):
    
    graph = get_graph(ancestors) #this will be used later for the get_graph

    s = Stack()
    s.push([starting_node])

    # keep track of [distance, node]
    earliest_node = [1
    , -1]

    while s.size() > 0:
        path = s.pop()
        last_node = path[-1]
        # print("path", path)
        # print("ln", last_node)

        # the eldest nodes (nodes at top of graph), are not in the dictionary, and are the end of the path
        if last_node not in graph:
            # check if path is longest and update our earliest_node tracker
            if len(path) > earliest_node[0]:
                earliest_node = [len(path), last_node]
            # "If there is more than one ancestor tied for "earliest", 
            # return the one with the lowest numeric ID."
            if len(path) == earliest_node[0] and last_node < earliest_node[1]:
                earliest_node = [len(path), last_node]
                # print("en", earliest_node)
        else:
            for n in graph[last_node]:
                s.push(path + [n])

    
    return earliest_node[1] 


def get_graph(ancestors):
    graph = {}
    for parent, child in ancestors:
        if child not in graph:
            graph[child] = []
        graph[child].append(parent)

    # print(graph)
    return graph

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    test2_ancestors = [(2, 3), (1, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # get_graph(test_ancestors)
    # {3: [1, 2], 6: [3, 5], 7: [5], 5: [4], 8: [4, 11], 9: [8], 1: [10]}
    print(earliest_ancestor(test_ancestors, 6))
    # print(earliest_ancestor(test2_ancestors, 6))