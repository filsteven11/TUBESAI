import heapq
import random

class IndoorNavigation:
    def __init__(self):
        self.graph = self.create_graph()

    def create_graph(self):
        graph = {
            # Floor 1
            'Entrance': {'Laboratorium Mac': 1},
            'Laboratorium Mac': {'Lift_F1': 1, 'Stairs_A_F1': 2, 'Laboratorium SI': 1},
            'Laboratorium SI': {'Laboratorium Mac': 1, 'Laboratorium DKV': 1},
            'Laboratorium DKV': {'Laboratorium SI': 1, 'Stairs_B_F1': 1},
            'Lift_F1': {'Lift_F2': 3, 'Stairs_A_F1': 1, 'Laboratorium Mac': 1},
            'Stairs_A_F1': {'Lift_F1': 1, 'Stairs_A_F2': 6, 'Laboratorium Mac': 2},
            'Stairs_B_F1': {'Stairs_B_F2': 6, 'Laboratorium DKV': 1},

            # Floor 2
            'Laboratorium Komputer': {'Lift_F2': 1, 'Stairs_A_F2': 2, 'Classroom 201': 1, 'Laboratorium Basis Data': 2},
            'Laboratorium Basis Data': {'Laboratorium Komputer': 2, 'Classroom 202': 1, 'Laboratorium Elektro': 2},
            'Laboratorium Elektro': {'Laboratorium Basis Data': 2, 'Classroom 204': 1, 'Stairs_B_F2': 1},
            'Classroom 201': {'Classroom 202': 1, 'Lift_F2': 1},
            'Classroom 202': {'Classroom 201': 1, 'Classroom 203': 1, 'Laboratorium Basis Data': 1},
            'Classroom 203': {'Classroom 202': 1, 'Classroom 204': 1},
            'Classroom 204': {'Classroom 203': 1, 'Classroom 205': 1, 'Laboratorium Elektro': 1},
            'Classroom 205': {'Classroom 204': 1, 'Stairs_B_F2': 1},
            'Lift_F2': {'Stairs_A_F2': 1, 'Lift_F1': 3, 'Lift_F3': 3, 'Laboratorium Komputer': 1, 'Classroom 201': 1},
            'Stairs_A_F2': {'Lift_F2': 1, 'Stairs_A_F1': 6, 'Stairs_A_F3': 6, 'Laboratorium Komputer': 2, 'Classroom 201': 2},
            'Stairs_B_F2': {'Stairs_B_F1': 6, 'Stairs_B_F3': 6, 'Laboratorium Elektro': 1, 'Classroom 205': 1},

            # Floor 3
            'Laboratorium CRC': {'Lift_F3': 1, 'Stairs_A_F3': 2, 'Classroom 301': 1, 'Laboratorium OLB': 2},
            'Laboratorium OLB': {'Laboratorium CRC': 2, 'Classroom 302': 1, 'Laboratorium IoT': 2},
            'Laboratorium IoT': {'Laboratorium OLB': 2, 'Classroom 304': 1, 'Stairs_B_F3': 1},
            'Classroom 301': {'Classroom 302': 1, 'Lift_F3': 1},
            'Classroom 302': {'Classroom 301': 1, 'Classroom 303': 1, 'Laboratorium OLB': 1},
            'Classroom 303': {'Classroom 302': 1, 'Classroom 304': 1},
            'Classroom 304': {'Classroom 303': 1, 'Classroom 305': 1, 'Laboratorium IoT': 1},
            'Classroom 305': {'Classroom 304': 1, 'Stairs_B_F3': 1},
            'Lift_F3': {'Stairs_A_F3': 1, 'Lift_F2': 3, 'Lift_F4': 3, 'Laboratorium CRC': 1, 'Classroom 301': 1},
            'Stairs_A_F3': {'Lift_F3': 1, 'Stairs_A_F2': 6, 'Stairs_A_F4': 6, 'Laboratorium CRC': 2, 'Classroom 301': 2},
            'Stairs_B_F3': {'Stairs_B_F2': 6, 'Stairs_B_F4': 6, 'Laboratorium IoT': 1, 'Classroom 305': 1},

            # Floor 4
            'Laboratorium Cyber': {'Lift_F4': 1, 'Stairs_A_F4': 2, 'Classroom 401': 1, 'Laboratorium Akuntansi': 2},
            'Laboratorium Akuntansi': {'Laboratorium Cyber': 2, 'Classroom 402': 1, 'Laboratorium ML': 2},
            'Laboratorium ML': {'Laboratorium Akuntansi': 2, 'Classroom 404': 1, 'Stairs_B_F4': 1},
            'Classroom 401': {'Classroom 402': 1, 'Lift_F4': 1},
            'Classroom 402': {'Classroom 401': 1, 'Classroom 403': 1, 'Laboratorium Akuntansi': 1},
            'Classroom 403': {'Classroom 402': 1, 'Classroom 404': 1},
            'Classroom 404': {'Classroom 403': 1, 'Classroom 405': 1, 'Laboratorium ML': 1},
            'Classroom 405': {'Classroom 404': 1, 'Stairs_B_F4': 1},
            'Lift_F4': {'Stairs_A_F4': 1, 'Lift_F3': 3, 'Laboratorium Cyber': 1, 'Classroom 401': 1},
            'Stairs_A_F4': {'Lift_F4': 1, 'Stairs_A_F3': 6, 'Laboratorium Cyber': 2, 'Classroom 401': 2},
            'Stairs_B_F4': {'Stairs_B_F3': 6, 'Laboratorium ML': 1, 'Classroom 405': 1},
        }
        return graph

    def block_access(self):
        access_points = ['Stairs_A_F1', 'Stairs_B_F1', 'Lift_F1', 
                         'Stairs_A_F2', 'Stairs_B_F2', 'Lift_F2', 
                         'Stairs_A_F3', 'Stairs_B_F3', 'Lift_F3', 
                         'Stairs_A_F4', 'Stairs_B_F4', 'Lift_F4']
        blocked_access = random.choice(access_points)
        
        # Remove connections for the blocked access point
        for node in self.graph:
            if blocked_access in self.graph[node]:
                del self.graph[node][blocked_access]
        
        print(f"Blocked access point: {blocked_access}")
        
    def dijkstra(self, start, end):
        queue = [(0, start)]  # (cost, node)
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        # Reconstruct the shortest path
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()

        return path, distances[end] if distances[end] != float('infinity') else None

    def find_shortest_path(self, start, end):
        path, cost = self.dijkstra(start, end)
        return path, cost
    
navigation = IndoorNavigation()
navigation.block_access()