import sys
from queue import Queue


def create_graph(shift_schedule, employees):
    graph = {}
    source = "source"
    sink = "sink"
    graph[source] = {}
    for station, (capacity, shifts) in shift_schedule.items():
        graph[source][station] = capacity # creating edge between source and stations wuth required num_staff
        for shift in shifts:
            # print(f"shift {shift}")
            graph.setdefault(station, {})[tuple(shift)] = capacity # creating edge between station and shifts with required num_staff
            graph.setdefault(tuple(shift), {})[sink] = 1 #connecting shifts with sink node to exit ?
    graph[sink] = {}
    for employee, (trained_stations, available_shifts) in employees.items():
        graph.setdefault(f"employee_{employee}", {})[sink] = 1 #creating edge between employees and sink node
        for station in trained_stations:
            shift_station = shift_schedule[station][1][0] #getting needed shift for that station
            if set(shift_station).issubset(set(available_shifts)): #checking if shift station is in available shifts of employee
                graph.setdefault(station, {})[f"employee_{employee}"] = 1 # creating edege
                

    return graph, source, sink


def bfs(graph, source, sink, parent):
    """
    basic bfs implementation with queue
    """
    visited = set()
    queue = Queue()
    queue.put(source)
    visited.add(source)

    while not queue.empty():
        u = queue.get()

        if u in graph:
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    queue.put(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
    return False


def ford_fulkerson(graph, source, sink):
    """
    ford fulkerson on the given graph
    """
    parent = {}
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        node_i = sink

        while node_i != source:
            path_flow = min(path_flow, graph[parent[node_i]][node_i])
            # print(f"going through node of {s} with a flow of {path_flow}")
            node_i = parent[node_i]

        max_flow += path_flow
        node_j = sink
        while node_j != source:
            u = parent[node_j]
            graph[u][node_j] -= path_flow
            if node_j in graph and u in graph[node_j]:
                graph[node_j][u] += path_flow
            else:
                graph[node_j][u] = path_flow
            node_j = parent[node_j]
    # print(f"maxflow= {parent}")
    return max_flow


def get_flow_path(parent, sink):
    path = []
    node = sink
    while node != "source":
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def calculate(shift_schedule, employees):
    graph, source, sink = create_graph(shift_schedule, employees)
    max_flow = ford_fulkerson(graph, source, sink)
    total_required = sum(num_required for num_required, _ in shift_schedule.values())
    print(f"total required: {total_required}, max flow: {max_flow}")
    # flow_path = get_flow_path(parent, sink)
    return max_flow == total_required


def parse_input(filename):
    with open(filename, "r") as file:
        shift_schedule = {}
        employees = {}
        mode = None
        is_in_employee = False

        for line in file:
            line = line.strip().split()
            if line[0] == "done":
                break
            elif line[0] in ("blend", "cook", "strain", "finish") and not is_in_employee: # checking if station
                mode = line[0]
                shift_schedule[mode] = [int(line[1]), []]
            elif line[0] == "employees" and not is_in_employee: # checking if line becomes staff details
                mode = "employees"
                is_in_employee = True
            elif is_in_employee:
                if mode in shift_schedule:
                    shift_schedule[mode][1].append(list(map(int, line)))
                elif mode == "employees":
                    trained_stations = line
                    available_shifts = list(map(int, file.readline().strip().split()))
                    employees[len(employees)] = (trained_stations, available_shifts)
            elif mode in shift_schedule:
                shift_schedule[mode][1].append(list(map(int, line)))

        return shift_schedule, employees


def main():
    filename = sys.argv[-1]
    shift_schedule, employees = parse_input(filename)
    result = calculate(shift_schedule, employees)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
