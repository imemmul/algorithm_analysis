import heapq
import sys
def subprime_path(capacity_graph, load_graph, start, end):
    # TODO Is below code able to handle cycles ??
    # TIME COMPLEXITY : O(mn)
    
    # load_graph[0][1] / capacity_graph[0][1] gives percentage of capacity if 1 then exit
    n = len(capacity_graph) # gives number of nodes
    # print(load_graph)
    # print(capacity_graph)
    cost_graph = [] # creating nxn matrix to keep overall cost and edges we have no negative edges so we can init with -1
    # update costs with laod_graph / capacity_graph
    for node in range(n):
        temp_list = []
        for neighbor in range(len(load_graph[node])):
            #print(f"float neighbor {float(load_graph[node][neighbor][1])}")
            direction_node = load_graph[node][neighbor][0]
            cost = float(load_graph[node][neighbor][1]) / float(capacity_graph[node][neighbor][1])
            temp_list.append((direction_node, cost))
        cost_graph.append(temp_list)
    # print(cost_graph) # now i have cost graph combined with capacity and load graph note: if cost is 1 then node is full capacity
    dist = [sys.maxsize] * n # initiliaze distance matrix with infinity
    prev = [None] * n  # to keep track of the previous node on the shortest path
    visited = [False] * n # visited matrix
    heap = [(0, start)] # run heap with given start node
    dist[start] = 0 # init start node distance with 0 

    while heap: # while heap is not empty
        curr_dist, curr_node = heapq.heappop(heap)
        visited[curr_node] = True

        if curr_node == end: # if we get end node finish
            break
        # print(prev)
        for neighbor, cost in cost_graph[curr_node]: # take next node and cost with it
            # cost = load_graph[curr_node][neighbor][1] / capacity_graph[curr_node][neighbor][1] out of range
            if cost != 1: # if capacity is full then dont take
                new_distance = dist[curr_node] + cost
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    prev[neighbor] = curr_node  # update the previous node on the shortest path
                    heapq.heappush(heap, (new_distance, neighbor)) # push new distance to heap

    # if prev[end] is None:
    #     return None # if there is prev[end] doesn't exist then return None as path
    # starting to save path
    
    path = []
    curr_node = end
    while curr_node != start:
        path.append(curr_node)
        curr_node = prev[curr_node]
    path.append(start)
    path.reverse()
    print(path)
    return path
    
def main():
    c = int(input())
    adjl_capacities = [[] for i in range(c)]
    adjl_loads = [[] for i in range(c)]
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_capacities[i].append((int(pair[0]),int(pair[1])))
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_loads[i].append((int(pair[0]),int(pair[1])))
    start = int(input())
    end=int(input())
    subprime_path(adjl_capacities,adjl_loads,start,end)

main()