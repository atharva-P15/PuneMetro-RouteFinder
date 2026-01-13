import heapq

def dijkstra(graph, start, end):
    distances = {station: float('inf') for station in graph}
    distances[start] = 0  

    queue = [(0, start, [start])]

    while queue:
        current_distance, current_station, path = heapq.heappop(queue)

        if current_station == end:
            return path, current_distance

        for neighbor in graph[current_station]:
            distance = current_distance + 2  

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor, path + [neighbor]))

    return None, float('inf')

""" old code:
import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        time, station, path = heapq.heappop(queue)
        if station in visited:
            continue
        visited.add(station)
        path = path + [station]

        if station == end:
            return path, time

        for neighbor in graph.get(station, []):
            if neighbor not in visited:
                heapq.heappush(queue, (time + 2, neighbor, path))

    return None, float('inf') """