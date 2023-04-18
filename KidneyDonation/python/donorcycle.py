
from collections import deque

def isInCycle(match_scores,donor_friends,query):
    n = len(match_scores[0]) # gives number of nodes (recipents) columns
    m = len(donor_friends) # gives number of donors rows
    # print(f"n {n}")
    # print(f"m {match_scores[2]}")
    # O(n^2) better than O(mn) so it is okay to use below line to create adj matrix
    # TIME COMPLEXITY : O(mn)
    adj_list = [[-1 for j in range(n)] for i in range(n)] # create 2D adj matrix with number of recipient init with -1
    for i in range(n):
        # print(adj_list)
        for j in range(m):
            # print(f"i {i}")
            # print(f"j {j}")
            if i == donor_friends[j] and match_scores[j][i] >=60:
                #donor friend takes donation
                #edge v to v ???? is it okay ?
                #dont need to edge between v to v so assigning None to it 
                adj_list[i][i] = None 
            elif match_scores[j][i] >= 60:
                #draw edge between recipent who takes donation and donor's friends
                adj_list[i][donor_friends[j]] = 1
            else:
                #no edge
                adj_list[i][donor_friends[j]] = 0
                    # print(f"i: {i} j: {j}")
    
    # print(adj_list)
    # Start BFS
    
    visited = [False] * n  # to keep track of visited nodes
    queue = deque() 

    queue.append(query)
    visited[query] = True

    while queue:
        # print(queue)
        # print(in_queue)
        curr_node = queue.popleft() # pop recently added recipent NOTE: using popleft() function actually works like stack ????
        for child in range(n):
            if adj_list[curr_node][child] == 1: # if there is a edge between recipent to recipent
                if not visited[child]: 
                    queue.append(child)
                    visited[child] = True
                elif visited[child]:
                    #if visited node is already visited than there is a cycle return True.
                    return True

    return False

def take_input():
    n = int(input()) # number of recipents
    m = int(input()) # number of donors
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []
    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    print(isInCycle(match_scores,donor_friends,query))

take_input()


