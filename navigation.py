import heapq
import random

class IndoorNavigation:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(IndoorNavigation, cls).__new__(cls)
            cls._instance.graph = cls._instance.create_graph()
            cls._instance.blocked_access = []  # Initialize blocked access points
        return cls._instance
    
    def __init__(self):
        self.graph = self.create_graph()

    def create_graph(self):
        graph = {
            # Floor 1
            'Entrance': {'Laboratorium Mac': 1},
            'Laboratorium Mac': {'Entrance': 1, 'Lift F1': 1, 'Left Stairs F1': 2, 'Laboratorium SI': 1},
            'Laboratorium SI': {'Laboratorium Mac': 1, 'Laboratorium DKV': 1},
            'Laboratorium DKV': {'Laboratorium SI': 1, 'Right Stairs F1': 1},
            'Lift F1': {'Lift F2': 3, 'Left Stairs F1': 1, 'Laboratorium Mac': 1},
            'Left Stairs F1': {'Lift F1': 1, 'Left Stairs F2': 6, 'Laboratorium Mac': 2},
            'Right Stairs F1': {'Right Stairs F2': 6, 'Laboratorium DKV': 1},

            # Floor 2
            'Laboratorium Komputer': {'Lift F2': 1, 'Left Stairs F2': 2, 'Class 201': 1, 'Laboratorium Basis Data': 2},
            'Laboratorium Basis Data': {'Laboratorium Komputer': 2, 'Class 202': 1, 'Laboratorium Elektro': 2},
            'Laboratorium Elektro': {'Laboratorium Basis Data': 2, 'Class 204': 1, 'Right Stairs F2': 1},
            'Class 201': {'Class 202': 1, 'Lift F2': 1},
            'Class 202': {'Class 201': 1, 'Class 203': 1, 'Laboratorium Basis Data': 1},
            'Class 203': {'Class 202': 1, 'Class 204': 1},
            'Class 204': {'Class 203': 1, 'Class 205': 1, 'Laboratorium Elektro': 1},
            'Class 205': {'Class 204': 1, 'Right Stairs F2': 1},
            'Lift F2': {'Left Stairs F2': 1, 'Lift F1': 3, 'Lift F3': 3, 'Laboratorium Komputer': 1, 'Class 201': 1},
            'Left Stairs F2': {'Lift F2': 1, 'Left Stairs F1': 6, 'Left Stairs F3': 6, 'Laboratorium Komputer': 2, 'Class 201': 2},
            'Right Stairs F2': {'Right Stairs F1': 6, 'Right Stairs F3': 6, 'Laboratorium Elektro': 1, 'Class 205': 1},

            # Floor 3
            'Laboratorium CRC': {'Lift F3': 1, 'Left Stairs F3': 2, 'Class 301': 1, 'Laboratorium OLB': 2},
            'Laboratorium OLB': {'Laboratorium CRC': 2, 'Class 302': 1, 'Laboratorium IoT': 2},
            'Laboratorium IoT': {'Laboratorium OLB': 2, 'Class 304': 1, 'Right Stairs F3': 1},
            'Class 301': {'Class 302': 1, 'Lift F3': 1},
            'Class 302': {'Class 301': 1, 'Class 303': 1, 'Laboratorium OLB': 1},
            'Class 303': {'Class 302': 1, 'Class 304': 1},
            'Class 304': {'Class 303': 1, 'Class 305': 1, 'Laboratorium IoT': 1},
            'Class 305': {'Class 304': 1, 'Right Stairs F3': 1},
            'Lift F3': {'Left Stairs F3': 1, 'Lift F2': 3, 'Lift F4': 3, 'Laboratorium CRC': 1, 'Class 301': 1},
            'Left Stairs F3': {'Lift F3': 1, 'Left Stairs F2': 6, 'Left Stairs F4': 6, 'Laboratorium CRC': 2, 'Class 301': 2},
            'Right Stairs F3': {'Right Stairs F2': 6, 'Right Stairs F4': 6, 'Laboratorium IoT': 1, 'Class 305': 1},

            # Floor 4
            'Laboratorium Cyber': {'Lift F4': 1, 'Left Stairs F4': 2, 'Class 401': 1, 'Laboratorium Akuntansi': 2},
            'Laboratorium Akuntansi': {'Laboratorium Cyber': 2, 'Class 402': 1, 'Laboratorium ML': 2},
            'Laboratorium ML': {'Laboratorium Akuntansi': 2, 'Class 404': 1, 'Right Stairs F4': 1},
            'Class 401': {'Class 402': 1, 'Lift F4': 1},
            'Class 402': {'Class 401': 1, 'Class 403': 1, 'Laboratorium Akuntansi': 1},
            'Class 403': {'Class 402': 1, 'Class 404': 1},
            'Class 404': {'Class 403': 1, 'Class 405': 1, 'Laboratorium ML': 1},
            'Class 405': {'Class 404': 1, 'Right Stairs F4': 1},
            'Lift F4': {'Left Stairs F4': 1, 'Lift F3': 3, 'Laboratorium Cyber': 1, 'Class 401': 1},
            'Left Stairs F4': {'Lift F4': 1, 'Left Stairs F3': 6, 'Laboratorium Cyber': 2, 'Class 401': 2},
            'Right Stairs F4': {'Right Stairs F3': 6, 'Laboratorium ML': 1, 'Class 405': 1},
        }
        return graph

    def block_access(self):
        access_points = [
            'Left Stairs F1', 'Right Stairs F1', 
            'Left Stairs F2', 'Right Stairs F2',
            'Left Stairs F3', 'Right Stairs F3', 
            'Left Stairs F4', 'Right Stairs F4',
            'Lift'
        ]
        
        blocked_access = random.choice(access_points)
        self.blocked_access.append(blocked_access)
        
        if blocked_access == 'Lift':
            lifts = ['Lift F1', 'Lift F2', 'Lift F3', 'Lift F4']
            for node in self.graph:
                for lift in lifts:
                    if lift in self.graph[node]:
                        del self.graph[node][lift]
        else:
            for node in self.graph:
                if blocked_access in self.graph[node]:
                    del self.graph[node][blocked_access]
        
        return blocked_access
    
    def dijkstra(self, start, goal):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)

            if current_node == goal:
                return path + [current_node], cost

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, edge_cost in self.graph.get(current_node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [current_node]))

        return None, float('inf')

    def find_shortest_path(self, start, end):
        path, cost = self.dijkstra(start, end)
        return path, cost