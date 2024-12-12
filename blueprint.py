import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button

def draw_floor(ax, floor_number, room_names=None):
    """Draw a single floor with rooms, stairs, lift, and entrance. Allow custom room names."""
    width, height = 12, 6
    room_width = width / 3
    F1R0 = height / 2
    F1R1 = height / 2
    F1R2 = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))
    entrance_width = 2
    ax.add_patch(patches.Rectangle((width / 2 - entrance_width / 2, 0), entrance_width, 1, edgecolor='black', facecolor='lightgrey'))
    ax.text(width / 2, -0.3, 'Entrance', ha='center', fontsize=10, weight='bold')

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    large_room_name = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, F1R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, large_room_name, ha='center', va='center', fontsize=10)

    storage_room_name = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, F1R1, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 4, height / 2 + F1R1 / 2, storage_room_name, ha='center', va='center', fontsize=9)

    office_room_name = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, F1R2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 2 + (room_width / 4), height / 2 + F1R2 / 2, office_room_name, ha='center', va='center', fontsize=9)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_second_floor(ax, floor_number, room_names=None):
    """Draw a second floor with 8 classrooms, stairs, lift, and restrooms."""
    width, height = 12, 6
    room_width = width / 5  # Width of each classroom
    room_height = height / 2  # Height of each classroom

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none ', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms (8 total) with a walkway between Classroom 1 and Classroom 5
    for i in range(4):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Walkway between Classroom 1 and Classroom 5
    ax.add_patch(patches.Rectangle((stair_width + 2 + 4 * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))  # Empty space for walkway
    ax.text(stair_width + 2 + 4 * room_width + room_width / 2, height / 2 + room_height / 2, 'Walkway', ha='center', va='center', fontsize=10, color='red')

    for i in range(4, 8):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + (i + 1) * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + (i + 1) * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Add WCs
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

# Function to draw the building with floor switching
def draw_building_with_switching(room_names=None):
    """Draw a building with multiple floors and buttons to switch between them."""
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.2)

    current_floor = [1]  # Use a list to allow modification in the button callback

    def update_floor(floor):
        ax.clear()  # Clear the current axes
        if floor == 1:
            draw_floor(ax, floor_number=1, room_names=room_names)
        else:
            draw_second_floor(ax, floor_number=2, room_names=room_names)
        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 7)
        ax .axis('off')  # Hide axes for a cleaner blueprint look
        plt.draw()  # Redraw the figure

    def switch_to_floor_1(event):
        current_floor[0] = 1
        update_floor(current_floor[0])

    def switch_to_floor_2(event):
        current_floor[0] = 2
        update_floor(current_floor[0])

    # Create buttons for switching floors
    ax_floor_1 = plt.axes([0.1, 0.05, 0.3, 0.075])
    ax_floor_2 = plt.axes([0.6, 0.05, 0.3, 0.075])
    btn_floor_1 = Button(ax_floor_1, 'Show Floor 1')
    btn_floor_2 = Button(ax_floor_2, 'Show Floor 2')

    btn_floor_1.on_clicked(switch_to_floor_1)
    btn_floor_2.on_clicked(switch_to_floor_2)

    # Initial drawing
    update_floor(current_floor[0])

    plt.show()

# Define custom room names for the floors
room_names = {
    'large_room': 'Laboratorium Komputer',
    'floor 1 room 1': 'Laboratorium SI',
    'floor 1 room 2': 'Laboratorium DKV',
    'classroom_1': 'Classroom 1',
    'classroom_2': 'Classroom 2',
    'classroom_3': 'Classroom 3',
    'classroom_4': 'Classroom 4',
    'classroom_5': 'Classroom 5',
    'classroom_6': 'Classroom 6',
    'classroom_7': 'Classroom 7',
    'classroom_8': 'Classroom 8'
}

# Run the function to draw the building with floor switching
draw_building_with_switching(room_names=room_names) 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button

def draw_floor(ax, floor_number, room_names=None):
    """Draw a single floor with rooms, stairs, lift, and entrance. Allow custom room names."""
    width, height = 12, 6
    room_width = width / 3
    F1R0 = height / 2
    F1R1 = height / 2
    F1R2 = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))
    entrance_width = 2
    ax.add_patch(patches.Rectangle((width / 2 - entrance_width / 2, 0), entrance_width, 1, edgecolor='black', facecolor='lightgrey'))
    ax.text(width / 2, -0.3, 'Entrance', ha='center', fontsize=10, weight='bold')

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    large_room_name = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, F1R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, large_room_name, ha='center', va='center', fontsize=10)

    storage_room_name = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, F1R1, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 4, height / 2 + F1R1 / 2, storage_room_name, ha='center', va='center', fontsize=9)

    office_room_name = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, F1R2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 2 + (room_width / 4), height / 2 + F1R2 / 2, office_room_name, ha='center', va='center', fontsize=9)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_second_floor(ax, floor_number, room_names=None):
    """Draw a second floor with 8 classrooms, stairs, lift, and restrooms."""
    width, height = 12, 6
    room_width = width / 5  # Width of each classroom
    room_height = height / 2  # Height of each classroom

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms (8 total) with a walkway between Classroom 1 and Classroom 5
    for i in range(4):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Walkway between Classroom 1 and Classroom 5
    ax.add_patch(patches.Rectangle((stair_width + 2 + 4 * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))  # Empty space for walkway
    ax.text(stair_width + 2 + 4 * room_width + room_width / 2, height / 2 + room_height / 2, 'Walkway', ha='center', va='center', fontsize=10, color='red')

    for i in range(4, 8):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + (i + 1) * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + (i + 1) * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Add WCs
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

# Function to draw the building with floor switching
def draw_building_with_switching(room_names=None):
    """Draw a building with multiple floors and buttons to switch between them."""
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.2)

    current_floor = [1]  # Use a list to allow modification in the button callback

    def update_floor(floor):
        ax.clear()  # Clear the current axes
        if floor == 1:
            draw_floor(ax, floor_number=1, room_names=room_names)
        else:
            draw_second_floor(ax, floor_number=2, room_names=room_names)
        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 7)
        ax.axis('off')  # Hide axes for a cleaner blueprint look
        plt.draw()  # Redraw the figure

    def switch_to_floor_1(event):
        current_floor[0] = 1
        update_floor(current_floor[0])

    def switch_to_floor_2(event):
        current_floor[ 0] = 2
        update_floor(current_floor[0])

    # Create buttons for switching floors
    ax_floor_1 = plt.axes([0.1, 0.05, 0.3, 0.075])
    ax_floor_2 = plt.axes([0.6, 0.05, 0.3, 0.075])
    btn_floor_1 = Button(ax_floor_1, 'Show Floor 1')
    btn_floor_2 = Button(ax_floor_2, 'Show Floor 2')

    btn_floor_1.on_clicked(switch_to_floor_1)
    btn_floor_2.on_clicked(switch_to_floor_2)

    # Initial drawing
    update_floor(current_floor[0])

    plt.show()

# Define custom room names for the floors
room_names = {
    'large_room': 'Laboratorium Komputer',
    'floor 1 room 1': 'Laboratorium SI',
    'floor 1 room 2': 'Laboratorium DKV',
    'classroom_1': 'Classroom 1',
    'classroom_2': 'Classroom 2',
    'classroom_3': 'Classroom 3',
    'classroom_4': 'Classroom 4',
    'classroom_5': 'Classroom 5',   
    'classroom_6': 'Classroom 6',
    'classroom_7': 'Classroom 7',
    'classroom_8': 'Classroom 8'
}

# Run the function to draw the building with floor switching
draw_building_with_switching(room_names=room_names)