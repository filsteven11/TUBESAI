import json
import tkinter as tk
from navigation import IndoorNavigation
import blueprint

def load_room_names(file_path):
    """Load room names from the specified JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['room_names']

def update_result_label(label, start_state, goal_state, shortest_path, cost):
    """Update the result label with the shortest path and total cost."""
    result_text = f"Shortest path from {start_state} to {goal_state}: {shortest_path} with total cost: {cost}"
    label.config(text=result_text)

def show_path_popup(start_state, goal_state, shortest_path, cost, blocked_path):
    """Display the path details in a new popup window."""
    popup = tk.Toplevel()
    popup.title("Path Details")

    path_label = tk.Label(popup, text="Path:", font=("Helvetica", 12))
    path_label.pack(pady=10)

    for room in shortest_path:
        room_label = tk.Label(popup, text=room, font=("Helvetica", 10))
        room_label.pack()

    blocked_label = tk.Label(popup, text=f"Blocked path: {blocked_path}", font=("Helvetica", 10))
    blocked_label.pack(pady=10)

    cost_label = tk.Label(popup, text=f"Total cost: {cost}", font=("Helvetica", 12, "bold"))
    cost_label.pack(pady=10)

    btn_close = tk.Button(popup, text="Close", command=popup.destroy)
    btn_close.pack(pady=10)


class RoomSelectionApp:
    def __init__(self, master, room_names, navigation):
        self.master = master
        self.master.title("Room Selection App")

        self.room_names = room_names
        self.start_state = None
        self.goal_state = None
        self.navigation = navigation

        self.start_frame = tk.Frame(self.master)
        self.goal_frame = tk.Frame(self.master)

        self.create_start_frame()
        self.create_goal_frame()

        self.start_frame.pack(fill="both", expand=True)

    def create_start_frame(self):
        label = tk.Label(self.start_frame, text="Select Start State:")
        label.pack()

        self.start_listbox = tk.Listbox(self.start_frame, selectmode=tk.BROWSE)
        for room in self.room_names.values():
            self.start_listbox.insert(tk.END, room)
        self.start_listbox.pack()

        btn_next = tk.Button(self.start_frame, text="Next", command=self.select_start_state)
        btn_next.pack()

    def create_goal_frame(self):
        label = tk.Label(self.goal_frame, text="Select Goal State:")
        label.pack()

        self.goal_listbox = tk.Listbox(self.goal_frame, selectmode=tk.BROWSE)
        for room in self.room_names.values():
            self.goal_listbox.insert(tk.END, room)
        self.goal_listbox.pack()

        btn_finish = tk.Button(self.goal_frame, text="Finish", command=self.select_goal_state)
        btn_finish.pack()

        btn_back = tk.Button(self.goal_frame, text="Back to Start", command=self.go_back_to_start)
        btn_back.pack()

    def go_back_to_start(self):
        self.goal_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

    def select_start_state(self):
        selected = self.start_listbox.curselection()
        if selected:
            self.start_state = self.start_listbox.get(selected)
            self.start_frame.pack_forget()
            self.goal_frame.pack(fill="both", expand=True)

    def select_goal_state(self):
        selected = self.goal_listbox.curselection()
        if selected:
            self.goal_state = self.goal_listbox.get(selected)
            self.master.quit()

            blocked_path = self.navigation.block_access()
            shortest_path, cost = self.navigation.find_shortest_path(self.start_state, self.goal_state)

            if shortest_path is not None:
                show_path_popup(self.start_state, self.goal_state, shortest_path, cost, blocked_path)
                starting_floor = blueprint.get_floor_from_room(self.start_state, room_names)
                blueprint.draw_building_with_switching(room_names=self.room_names, start_floor=starting_floor, start_room=self.start_state, goal_room=self.goal_state)
            else:
                print(f"No path found from {self.start_state} to {self.goal_state}.")

navigation = IndoorNavigation()
room_names = load_room_names('room_names.json')

root = tk.Tk()
app = RoomSelectionApp(root, room_names, navigation)
root.mainloop()
