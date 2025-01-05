import json
import tkinter as tk
from navigation import IndoorNavigation

def load_room_names(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['room_names']

class RoomSelectionApp:
    def __init__(self, master, room_names):
        self.master = master
        self.master.title("Room Selection App")
        
        self.room_names = room_names
        self.start_state = None
        self.goal_state = None
        
        # Create frames for each page
        self.start_frame = tk.Frame(self.master)
        self.goal_frame = tk.Frame(self.master)

        # Initialize the start state selection frame
        self.create_start_frame()

        # Initialize the goal state selection frame
        self.create_goal_frame()

        # Show the start frame initially
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

    def select_start_state(self):
        selected = self.start_listbox.curselection()
        if selected:
            self.start_state = self.start_listbox.get(selected)
            self.start_frame.pack_forget()  # Hide start frame
            self.goal_frame.pack(fill="both", expand=True)  # Show goal frame

    def select_goal_state(self):
        selected = self.goal_listbox.curselection()
        if selected:
            self.goal_state = self.goal_listbox.get(selected)
            print(f"Selected Start State: {self.start_state}, Selected Goal State: {self.goal_state}")
            self.master.quit()  # Close the application after selection
            
            # After user selects start and goal states
            navigation = IndoorNavigation()
            shortest_path, cost = navigation.find_shortest_path(self.start_state, self.goal_state)
            if shortest_path is not None:
                print(f"Shortest path from {self.start_state} to {self.goal_state}: {shortest_path} with total cost: {cost}")
            else:
                print(f"No path found from {self.start_state} to {self.goal_state}.")


# Load room names from the JSON file
room_names = load_room_names('room_names.json')

# Create the main application window
root = tk.Tk()
app = RoomSelectionApp(root, room_names)

# Start the Tkinter main loop
root.mainloop()