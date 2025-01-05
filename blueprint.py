import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button, CheckButtons
import random
import json
import time
import tkinter as tk
from tkinter import messagebox

def load_room_names(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['room_names']

def draw_pinpoint(ax, x, y, label):
    """Draw a pinpoint at the specified location."""
    ax.plot(x, y, 'ro')  # Red dot
    ax.text(x, y + 0.2, label, ha='center', fontsize=8, color='black')

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

    # Draw pin for entrance
    draw_pinpoint(ax, width / 2, 0.5, 'Entrance')

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw rooms and pinpoints
    labkom = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, F1R0, edgecolor='black', facecolor='none'))
    # ax.text(stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, labkom, ha='center', va='center', fontsize=10)
    draw_pinpoint(ax, stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, labkom)

    labsi = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, F1R1, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, stair_width + 2 + room_width + room_width / 4, height / 2 + F1R1 / 2, labsi)

    labdkv = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, F1R2, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, stair_width + 2 + room_width + room_width / 2 + (room_width / 4), height / 2 + F1R2 / 2, labdkv)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_second_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 2 classroom_{i+201}', f'Classroom {i+201}') if room_names else f'Classroom {i+201}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        draw_pinpoint(ax, stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, 0.5, 0.75, 'WC')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, width - 0.5, 0.75, 'WC')

    # Draw Lab and pinpoints
    F2R0 = height / 4
    labkom = room_names.get('floor 2 room 1', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, stair_width + 0.75 + room_width / 2, F2R0 / 2, labkom)

    labbasdat = room_names.get('floor 2 room 2', 'Laboratorium Basis Data') if room_names else 'Laboratorium Basis Data'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, stair_width + 4 + room_width / 2, F2R0 / 2, labbasdat)

    labelektro = room_names.get('floor 2 room 3', 'Laboratorium Elektro') if room_names else 'Laboratorium Elektro'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, F2R0, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, stair_width + 7.5 + room_width / 2, F2R0 / 2, labelektro)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_third_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 3 classroom_{i+301}', f'Classroom {i+301}') if room_names else f'Classroom {i+301}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        draw_pinpoint(ax, stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, 0.5, 0.75, 'WC')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, width - 0.5, 0.75, 'WC')

    # Draw Labs and pinpoints
    lab_crc = room_names.get('floor 3 room 1', 'Laboratorium CRC') if room_names else 'Laboratorium CRC'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + room_width, height / 8, lab_crc)

    lab_olb = room_names.get('floor 3 room 2', 'Laboratorium OLB') if room_names else 'Laboratorium OLB'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + 3 * room_width, height / 8, lab_olb)

    lab_iot = room_names.get('floor 3 room 3', 'Laboratorium IoT') if room_names else 'Laboratorium IoT'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + 5.125 * room_width, height / 8, lab_iot)

    ax.text(width / 2, height + 0.5, f"Floor {floor_number}", ha='center', fontsize=12, weight='bold')

def draw_fourth_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5 
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=2))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue'))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=9, weight='bold')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen'))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=9, weight='bold')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 4 classroom_{i+401}', f'Classroom {i+401}') if room_names else f'Classroom {i+401}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none'))
        draw_pinpoint(ax, stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, 0.5, 0.75, 'WC')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey'))
    draw_pinpoint(ax, width - 0.5, 0.75, 'WC')

    # Draw Labs and pinpoints
    lab_cyber = room_names.get('floor 4 room 1', 'Laboratorium Cyber') if room_names else 'Laboratorium Cyber'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + room_width, height / 8, lab_cyber)

    lab_accounting = room_names.get('floor 4 room 2', 'Laboratorium Akuntansi') if room_names else 'Laboratorium Akuntansi'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + 3 * room_width, height / 8, lab_accounting)

    lab_ml = room_names.get('floor 4 room 3', 'Laboratorium ML') if room_names else 'Laboratorium ML'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, height / 4, edgecolor='black', facecolor='none'))
    draw_pinpoint(ax, wc_width + 5.125 * room_width, height / 8, lab_ml)

    ax.text(width / 2, height + 0.5, f"Floor {floor_number}", ha='center', fontsize=12, weight='bold')
    
#switch floor
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

    # Displaying the plot
    update_floor(current_floor[0])
    plt.show()

def generate_random_time():
    # Generate random hour and minute
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    
    # Format time as HH:MM
    return f"{random_hour:02}:{random_minute:02}"

# Create a tkinter window to display the random time
def display_random_time():
    random_time = generate_random_time()  # Generate a random time
    root = tk.Tk()  # Create a new Tkinter window
    root.title("Random Time Display")

    # Add label with the random time
    label = tk.Label(root, text=f"Random Time: {random_time}", font=('Helvetica', 14))
    label.pack(pady=20)

    # Add an OK button to close the window
    button = tk.Button(root, text="OK", command=root.quit)
    button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to display the random time in a new window
display_random_time()

room_names = load_room_names('room_names.json')

draw_building_with_switching(room_names=room_names)
