import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button,CheckButtons



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

    labkom = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, F1R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, labkom, ha='center', va='center', fontsize=10)

    labsi = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, F1R1, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 4, height / 2 + F1R1 / 2, labsi, ha='center', va='center', fontsize=9)

    labdkv = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, F1R2, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 2 + room_width + room_width / 2 + (room_width / 4), height / 2 + F1R2 / 2, labdkv, ha='center', va='center', fontsize=9)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_second_floor(ax, floor_number, room_names=None):
    """Draw a second floor with 8 classrooms, stairs, lift, and restrooms."""
    width, height = 12, 6
    room_width = width / 7.5  # Width of each classroom
    room_height = height / 2  # Height of each classroom

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms (5 total)
    for i in range(5):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Add WCs
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')
        
    # Draw Lab 
    F2R0 = height / 4
    F2R1 = height / 4
    F2R2 = height / 4
    labkom = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 0.75 + room_width / 2, F2R0 / 2, labkom, ha='center', va='center', fontsize=10)

    labbasdat = room_names.get('floor 2 room 1', 'Laboratorium Basis Data') if room_names else 'Laboratorium Basis Data'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 4 + room_width / 2, F2R0 / 2, labbasdat, ha='center', va='center', fontsize=10)
    
    labelektro = room_names.get('floor 2 room 2', 'Laboratorium Elektro') if room_names else 'Laboratorium Elektro'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, F2R0, edgecolor='black', facecolor='none'))
    ax.text(stair_width + 7.5 + room_width / 2, F2R0 / 2, labelektro, ha='center', va='center', fontsize=10)
    
    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_third_floor(ax, floor_number, room_names=None):
    """Draw a third floor with 8 classrooms, stairs, lift, and restrooms."""
    width, height = 12, 6
    room_width = width / 7.5  # Width of each classroom
    room_height = height / 2  # Height of each classroom

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms (5 total)
    for i in range(5):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Add WCs
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    # Draw Labs
    lab_crc = room_names.get('large_room', 'Laboratorium CRC') if room_names else 'Laboratorium CRC'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + room_width, height / 8, lab_crc, ha='center', va='center', fontsize=10)

    lab_olb = room_names.get('floor_3_room_1', 'Laboratorium OLB') if room_names else 'Laboratorium OLB'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + 3 * room_width, height / 8, lab_olb, ha='center', va='center', fontsize=10)

    lab_iot = room_names.get('floor_3_room_2', 'Laboratorium IoT') if room_names else 'Laboratorium IoT'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + 5.125 * room_width, height / 8, lab_iot, ha='center', va='center', fontsize=10)

    ax.text(width / 2, height + 0.5, f"Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_fourth_floor(ax, floor_number, room_names=None):
    """Draw a fourth floor with labs and classrooms."""
    width, height = 12, 6
    room_width = width / 7.5  # Width of each classroom
    room_height = height / 2  # Height of each classroom

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms (5 total)
    for i in range(5):
        room_name = room_names.get(f'classroom_{i+1}', f'Classroom {i+1}') if room_names else f'Classroom {i+1}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=10)

    # Add WCs
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=9, weight='bold')

    # Draw Labs
    lab_cyber = room_names.get('large_room', 'Laboratorium Cyber') if room_names else 'Laboratorium Cyber'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + room_width, height / 8, lab_cyber, ha='center', va='center', fontsize=10)

    lab_accounting = room_names.get('floor_4_room_1', 'Laboratorium Akuntansi') if room_names else 'Laboratorium Akuntansi'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + 3 * room_width, height / 8, lab_accounting, ha='center', va='center', fontsize=10)

    lab_ml = room_names.get('floor_4_room_2', 'Laboratorium ML') if room_names else 'Laboratorium ML'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, height / 4, edgecolor='black', facecolor='none'))
    ax.text(wc_width + 5.125 * room_width, height / 8, lab_ml, ha='center', va='center', fontsize=10)

    ax.text(width / 2, height + 0.5, f"Floor {floor_number}", ha='center', fontsize=12, weight='bold')
    ##switch floor

def draw_building_with_switching(room_names=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.3)

    current_floor = [1]

    def update_floor(floor):
        ax.clear()
        if floor == 1:
            draw_floor(ax, floor_number=1, room_names=room_names)
        elif floor == 2:
            draw_second_floor(ax, floor_number=2, room_names=room_names)
        elif floor == 3:
            draw_third_floor(ax, floor_number=3, room_names=room_names)
        elif floor == 4:
            draw_fourth_floor(ax, floor_number=4, room_names=room_names)

        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 7)
        ax.axis('off')
        plt.draw()

        # Update checklist based on current floor
        update_checklist(floor)

    def switch_floor(delta):
        new_floor = current_floor[0] + delta
        if 1 <= new_floor <= 4:
            current_floor[0] = new_floor
            update_floor(current_floor[0])

    # Buttons for navigation
    ax_prev = plt.axes([0.1, 0.05, 0.3, 0.075])
    ax_next = plt.axes([0.6, 0.05, 0.3, 0.075])
    btn_prev = Button(ax_prev, 'Previous Floor')
    btn_next = Button(ax_next, 'Next Floor')

    btn_prev.on_clicked(lambda event: switch_floor(-1))
    btn_next.on_clicked(lambda event: switch_floor(1))

    # Checklists for the floors
    ax_checklist = plt.axes([0.05, 0.2, 0.3, 0.15])
    checklist_labels = []

    # Define room names for checklists
    if current_floor[0] == 1:
        checklist_labels = ['Laboratorium Komputer', 'Laboratorium SI', 'Laboratorium DKV']
    elif current_floor[0] == 2:
        checklist_labels = [
            'Laboratorium Basis Data', 'Laboratorium Elektro',
            'Classroom 1', 'Classroom 2', 'Classroom 3', 'Classroom 4', 'Classroom 5'
            
        ]
    elif current_floor[0] == 3:
        checklist_labels = [
            'Laboratorium CRC', 'Laboratorium OLB', 'Laboratorium IoT',
            'Classroom 1', 'Classroom 2', 'Classroom 3', 'Classroom 4', 'Classroom 5'
        ]
    elif current_floor[0] == 4:
        checklist_labels = [
            'Laboratorium Cyber', 'Laboratorium Akuntansi', 'Laboratorium ML',
            'Classroom 1', 'Classroom 2', 'Classroom 3', 'Classroom 4', 'Classroom 5'
            
        ]
    
    checklist = CheckButtons(ax_checklist, checklist_labels, [False] * len(checklist_labels))

    def update_checklist(floor):
        if floor == 1:
            checklist.set_active([True, True, True])
        elif floor == 2:
            checklist.set_active([True, True, True, True, True, True, True] )  
        elif floor == 3:
            checklist.set_active([True, True, True, True, True, True, True])  
        elif floor == 4:
            checklist.set_active([True, True, True, True, True, True, True]) 

    update_floor(current_floor[0])
    plt.show()

room_names = {
    'large_room': 'Laboratorium Komputer',
    'floor 1 room 1': 'Laboratorium SI',
    'floor 1 room 2': 'Laboratorium DKV',
    'floor 2 room 1': 'Laboratorium Basis Data',
    'floor 2 room 2': 'Laboratorium Elektro',
    'floor 3 room 1': 'Laboratorium CRC',
    'floor 3 room 2': 'Laboratorium OLB',
    'floor 4 room 1': 'Laboratorium Cyber',
    'floor 4 room 2': 'Laboratorium Akuntansi',
    'floor 4 room 3': 'Laboratorium ML',
    # Add more room names as needed
}

# Run the function to draw the building with floor switching and checklists
draw_building_with_switching(room_names=room_names)
