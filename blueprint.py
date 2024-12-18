import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button

def draw_floor(ax, floor_number, room_names=None):
    """Draw a single floor with rooms, stairs, lift, and entrance."""
    width, height = 12, 6
    room_width = width / 3

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    # Entrance
    entrance_width = 2
    ax.add_patch(patches.Rectangle((width / 2 - entrance_width / 2, 0), entrance_width, 1, edgecolor='black', facecolor='lightgrey'))
    ax.text(width / 2, -0.3, 'Entrance', ha='center', fontsize=10, weight='bold')

    # Stairs and lift (Positioned symmetrically)
    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Rooms (Laboratorium and Classrooms)
    room_1_name = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, height / 2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width / 2, height / 2 + height / 4, room_1_name, ha='center', va='center', fontsize=10)

    room_2_name = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, height / 2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 4, height / 2 + height / 4, room_2_name, ha='center', va='center', fontsize=9)

    room_3_name = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, height / 2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 2 + room_width / 4, height / 2 + height / 4, room_3_name, ha='center', va='center', fontsize=9)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_second_floor(ax, floor_number, room_names=None):
    """Draw the second floor with classrooms and proper positioning of stairs, lift, and restrooms."""
    width, height = 12, 6
    room_width = width / 5  # 5 units per width for classrooms
    room_height = height / 4  # Room height
    pathway_height = 1  # Height of the pathway in the middle
    space_between_rows = 0.5  # Space between the top and bottom sections

    # Draw the entire floor boundary
    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    # Draw the top section (Upper half of the floor)
    # Draw the pathway in the middle (correct space between top and bottom section)
    ax.add_patch(patches.Rectangle((0, height / 2 - pathway_height / 2), width, pathway_height, edgecolor='black', facecolor='lightgrey'))

    # Draw stairs and lift (Positioned symmetrically at the ends of the floor)
    stair_width = room_width / 2  # Slightly smaller
    stair_height = 1.2
    lift_width = stair_width
    lift_height = stair_height

    # Positioning stairs and lift to align with classrooms 1-4
    stair_x = room_width  # Positioned next to the first classroom (Class 1)
    lift_x = stair_x + stair_width  # Positioned next to the stairs

    # Stairs (Positioned at the left)
    ax.add_patch(patches.Rectangle((stair_x, height / 2), stair_width, stair_height, edgecolor='black', facecolor='lightblue'))
    ax.text(stair_x + stair_width / 2, height / 2 + stair_height / 2, 'Stairs', ha='center', va='center', fontsize=9)

    # Lift (Positioned next to the stairs)
    ax.add_patch(patches.Rectangle((lift_x, height / 2), lift_width, lift_height, edgecolor='black', facecolor='lightgreen'))
    ax.text(lift_x + lift_width / 2, height / 2 + lift_height / 2, 'Lift', ha='center', va='center', fontsize=9)

    # Classrooms 1 to 4 (Top row, aligned with stairs and lift)
    for i in range(4):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        x = (i + 2) * room_width  # Adjusted to leave space for stairs and lift
        ax.add_patch(patches.Rectangle((x, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(x + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=9)

    # Draw the bottom section (Lower half of the floor)
    # Adjust space between the top and bottom rows
    bottom_section_y = height / 2 - space_between_rows - room_height

    # Restrooms (near the classrooms)
    restroom_width = stair_width + lift_width  # WC size same as the combined size of Lift and Stairs
    restroom_height = room_height

    # WC near Classroom 5 (left side)
    ax.add_patch(patches.Rectangle((room_width / 2 - restroom_width / 2, bottom_section_y), restroom_width, restroom_height, edgecolor='black', facecolor='lightblue'))
    ax.text(room_width / 2, bottom_section_y + restroom_height / 2, 'WC', ha='center', va='center', fontsize=9)

    # Classrooms 5 to 8 (Bottom row, between the restrooms)
    for i in range(4):
        room_name = room_names.get(f'classroom_{i+5}', f'Classroom {i+5}') if room_names else f'Classroom {i+5}'
        x = (i + 1) * room_width  # Adjusted to leave space for WC and classrooms
        ax.add_patch(patches.Rectangle((x, bottom_section_y), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(x + room_width / 2, bottom_section_y + room_height / 2, room_name, ha='center', va='center', fontsize=9)

    # Add title for the floor
    ax.text(width / 2, height + 0.5, f"Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_building_with_switching(room_names=None):
    """Draw a building with multiple floors and buttons to switch between them."""
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.2)

    current_floor = [1]

    def update_floor(floor):
        ax.clear()
        if floor == 1:
            draw_floor(ax, floor_number=1, room_names=room_names)
        elif floor == 2:
            draw_second_floor(ax, floor_number=2, room_names=room_names)
        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 7)
        ax.axis('off')
        plt.draw()

    def switch_to_floor_1(event):
        current_floor[0] = 1
        update_floor(current_floor[0])

    def switch_to_floor_2(event):
        current_floor[0] = 2
        update_floor(current_floor[0])

    ax_floor_1 = plt.axes([0.1, 0.05, 0.3, 0.075])
    ax_floor_2 = plt.axes([0.6, 0.05, 0.3, 0.075])
    btn_floor_1 = Button(ax_floor_1, 'Show Floor 1')
    btn_floor_2 = Button(ax_floor_2, 'Show Floor 2')

    btn_floor_1.on_clicked(switch_to_floor_1)
    btn_floor_2.on_clicked(switch_to_floor_2)

    update_floor(current_floor[0])
    plt.show()

# Room names for customization
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

# Run the application
draw_building_with_switching(room_names=room_names)
