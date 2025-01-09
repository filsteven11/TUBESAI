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
            'Entrance': {'Laboratorium Mac': 2},
            'Laboratorium Mac': {'Entrance': 2, 'Lift F1': 2, 'Left Stairs F1': 4, 'Laboratorium SI': 2},
            'Laboratorium SI': {'Laboratorium Mac': 2, 'Laboratorium DKV': 2},
            'Laboratorium DKV': {'Laboratorium SI': 2, 'Right Stairs F1': 2},
            'Lift F1': {'Lift F2': 3, 'Left Stairs F1': 2, 'Laboratorium Mac': 2},
            'Left Stairs F1': {'Lift F1': 2, 'Left Stairs F2': 12, 'Laboratorium Mac': 4},
            'Right Stairs F1': {'Right Stairs F2': 12, 'Laboratorium DKV': 2},

            # Floor 2
            'Laboratorium Komputer': {'Lift F2': 2, 'Left Stairs F2': 4, 'Class 201': 2, 'Laboratorium Basis Data': 4},
            'Laboratorium Basis Data': {'Laboratorium Komputer': 4, 'Class 202': 2, 'Laboratorium Elektro': 4},
            'Laboratorium Elektro': {'Laboratorium Basis Data': 4, 'Class 204': 2, 'Right Stairs F2': 2},
            'Class 201': {'Class 202': 2, 'Lift F2': 2},
            'Class 202': {'Class 201': 2, 'Class 203': 2, 'Laboratorium Basis Data': 2},
            'Class 203': {'Class 202': 2, 'Class 204': 2},
            'Class 204': {'Class 203': 2, 'Class 205': 2, 'Laboratorium Elektro': 2},
            'Class 205': {'Class 204': 2, 'Right Stairs F2': 2},
            'Lift F2': {'Left Stairs F2': 2, 'Lift F1': 3, 'Lift F3': 3, 'Laboratorium Komputer': 2, 'Class 201': 2},
            'Left Stairs F2': {'Lift F2': 2, 'Left Stairs F1': 12, 'Left Stairs F3': 12, 'Laboratorium Komputer': 4, 'Class 201': 4},
            'Right Stairs F2': {'Right Stairs F1': 12, 'Right Stairs F3': 12, 'Laboratorium Elektro': 2, 'Class 205': 2},

            # Floor 3
            'Laboratorium CRC': {'Lift F3': 2, 'Left Stairs F3': 4, 'Class 301': 2, 'Laboratorium OLB': 4},
            'Laboratorium OLB': {'Laboratorium CRC': 4, 'Class 302': 2, 'Laboratorium IoT': 4},
            'Laboratorium IoT': {'Laboratorium OLB': 4, 'Class 304': 2, 'Right Stairs F3': 2},
            'Class 301': {'Class 302': 2, 'Lift F3': 2},
            'Class 302': {'Class 301': 2, 'Class 303': 2, 'Laboratorium OLB': 2},
            'Class 303': {'Class 302': 2, 'Class 304': 2},
            'Class 304': {'Class 303': 2, 'Class 305': 2, 'Laboratorium IoT': 2},
            'Class 305': {'Class 304': 2, 'Right Stairs F3': 2},
            'Lift F3': {'Left Stairs F3': 2, 'Lift F2': 3, 'Lift F4': 3, 'Laboratorium CRC': 2, 'Class 301': 2},
            'Left Stairs F3': {'Lift F3': 2, 'Left Stairs F2': 12, 'Left Stairs F4': 12, 'Laboratorium CRC': 4, 'Class 301': 4},
            'Right Stairs F3': {'Right Stairs F2': 12, 'Right Stairs F4': 12, 'Laboratorium IoT': 2, 'Class 305': 2},

            # Floor 4
            'Laboratorium Cyber': {'Lift F4': 2, 'Left Stairs F4': 4, 'Class 401': 2, 'Laboratorium Akuntansi': 4},
            'Laboratorium Akuntansi': {'Laboratorium Cyber': 4, 'Class 402': 2, 'Laboratorium ML': 4},
            'Laboratorium ML': {'Laboratorium Akuntansi': 4, 'Class 404': 2, 'Right Stairs F4': 2},
            'Class 401': {'Class 402': 2, 'Lift F4': 2},
            'Class 402': {'Class 401': 2, 'Class 403': 2, 'Laboratorium Akuntansi': 2},
            'Class 403': {'Class 402': 2, 'Class 404': 2},
            'Class 404': {'Class 403': 2, 'Class 405': 2, 'Laboratorium ML': 2},
            'Class 405': {'Class 404': 2, 'Right Stairs F4': 2},
            'Lift F4': {'Left Stairs F4': 2, 'Lift F3': 3, 'Laboratorium Cyber': 2, 'Class 401': 2},
            'Left Stairs F4': {'Lift F4': 2, 'Left Stairs F3': 12, 'Laboratorium Cyber': 4, 'Class 401': 4},
            'Right Stairs F4': {'Right Stairs F3': 12, 'Laboratorium ML': 2, 'Class 405': 2},
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