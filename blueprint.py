import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
import json

def load_room_names(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['room_names']



def draw_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 3
    F1R0 = height / 2
    F1R1 = height / 2
    F1R2 = height / 2

    # Background and outer border
    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='lightyellow', lw=2, zorder=0))

    # Entrance
    entrance_width = 2
    ax.add_patch(patches.Rectangle((width / 2 - entrance_width / 2, 0), entrance_width, 1, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(width / 2, -0.3, 'Entrance', ha='center', fontsize=12, weight='bold', color='black')

    # Stairs
    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')

    # Lift
    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen', lw=2, zorder=1))
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=11, weight='bold', color='black')

    # Rooms and pinpoints
    labkom = room_names.get('large_room', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((stair_width + 2, height / 2), room_width, F1R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 2 + room_width / 2, height / 2 + F1R0 / 2, labkom, ha='center', va='center', fontsize=12, zorder=2)

    labsi = room_names.get('floor 1 room 1', 'Laboratorium SI') if room_names else 'Laboratorium SI'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width, height / 2), room_width / 2, F1R1, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 2 + room_width + room_width / 4, height / 2 + F1R1 / 2, labsi, ha='center', va='center', fontsize=11, zorder=2)

    labdkv = room_names.get('floor 1 room 2', 'Laboratorium DKV') if room_names else 'Laboratorium DKV'
    ax.add_patch(patches.Rectangle((stair_width + 2 + room_width + room_width / 2, height / 2), room_width / 2, F1R2, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 2 + room_width + room_width / 2 + (room_width / 4), height / 2 + F1R2 / 2, labdkv, ha='center', va='center', fontsize=9, zorder=2)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=14, weight='bold', color='black', zorder=3)

def draw_second_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='lightyellow', lw=2, zorder=0))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen', lw=2, zorder=1))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 2 class_{i+201}', f'Class {i+201}') if room_names else f'Class {i+201}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none', lw=2, zorder=1))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=12, zorder=2)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Lab and pinpoints
    F2R0 = height / 4
    labkom = room_names.get('floor 2 room 1', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 0.75 + room_width / 2, F2R0 / 2, labkom, ha='center', va='center', fontsize=12, zorder=2)

    labbasdat = room_names.get('floor 2 room 2', 'Laboratorium Basis Data') if room_names else 'Laboratorium Basis Data'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, F2R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 4 + room_width / 2, F2R0 / 2, labbasdat, ha='center', va='center', fontsize=12, zorder=2)

    labelektro = room_names.get('floor 2 room 3', 'Laboratorium Elektro') if room_names else 'Laboratorium Elektro'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, F2R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 7.5 + room_width / 2, F2R0 / 2, labelektro, ha='center', va='center', fontsize=12, zorder=2)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=14, weight='bold', color='black', zorder=3)


def draw_third_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='lightyellow', lw=2, zorder=0))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen', lw=2, zorder=1))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 3 class {i+301}', f'Class {i+301}') if room_names else f'class{i+301}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none', lw=2, zorder=1))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=12, zorder=2)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Labs and pinpoints
    F3R0 = height / 4
    labkom = room_names.get('floor 3 room 1', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, F3R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 0.75 + room_width / 2, F3R0 / 2, labkom, ha='center', va='center', fontsize=12, zorder=2)

    labbasdat = room_names.get('floor 3 room 2', 'Laboratorium Basis Data') if room_names else 'Laboratorium Basis Data'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, F3R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 4 + room_width / 2, F3R0 / 2, labbasdat, ha='center', va='center', fontsize=12, zorder=2)

    labelektro = room_names.get('floor 3 room 3', 'Laboratorium Elektro') if room_names else 'Laboratorium Elektro'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, F3R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 7.5 + room_width / 2, F3R0 / 2, labelektro, ha='center', va='center', fontsize=12, zorder=2)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=14, weight='bold', color='black', zorder=3)


def draw_fourth_floor(ax, floor_number, room_names=None):
    width, height = 12, 6
    room_width = width / 7.5
    room_height = height / 2

    ax.add_patch(patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='lightyellow', lw=2, zorder=0))

    stair_width = 1
    ax.add_patch(patches.Rectangle((0, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Left stair
    ax.add_patch(patches.Rectangle((width - stair_width, height / 2), stair_width, 1.5, edgecolor='black', facecolor='lightblue', lw=2, zorder=1))  # Right stair
    ax.text(0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Left stair label
    ax.text(width - 0.5, height / 2 + 1.6, 'Stairs', ha='center', fontsize=11, weight='bold', color='black')  # Right stair label

    ax.add_patch(patches.Rectangle((stair_width, height / 2), 2, 1.5, edgecolor='black', facecolor='lightgreen', lw=2, zorder=1))  # Lift
    ax.text(stair_width + 1, height / 2 + 1.6, 'Lift', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Classrooms and pinpoints
    for i in range(5):
        room_name = room_names.get(f'floor 4 class{i+401}', f'Class {i+401}') if room_names else f'Class{i+401}'
        ax.add_patch(patches.Rectangle((stair_width + 2 + i * room_width, height / 2), room_width, room_height, edgecolor='black', facecolor='none', lw=2, zorder=1))
        ax.text(stair_width + 2 + i * room_width + room_width / 2, height / 2 + room_height / 2, room_name, ha='center', va='center', fontsize=12, zorder=2)

    # Add WCs and pinpoints
    wc_width = 1
    ax.add_patch(patches.Rectangle((0, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    ax.add_patch(patches.Rectangle((width - wc_width, 0), wc_width, 1.5, edgecolor='black', facecolor='lightgrey', lw=2, zorder=1))
    ax.text(width - 0.5, 0.75, 'WC', ha='center', fontsize=11, weight='bold', color='black')

    # Draw Labs and pinpoints
    F4R0 = height / 4
    labkom = room_names.get('floor 4 room 1', 'Laboratorium Komputer') if room_names else 'Laboratorium Komputer'
    ax.add_patch(patches.Rectangle((wc_width, 0), room_width * 2, F4R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 0.75 + room_width / 2, F4R0 / 2, labkom, ha='center', va='center', fontsize=12, zorder=2)

    labbasdat = room_names.get('floor 4 room 2', 'Laboratorium Basis Data') if room_names else 'Laboratorium Basis Data'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 2, 0), room_width * 2, F4R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 4 + room_width / 2, F4R0 / 2, labbasdat, ha='center', va='center', fontsize=12, zorder=2)

    labelektro = room_names.get('floor 4 room 3', 'Laboratorium Elektro') if room_names else 'Laboratorium Elektro'
    ax.add_patch(patches.Rectangle((wc_width + room_width * 4, 0), room_width * 2.25, F4R0, edgecolor='black', facecolor='none', lw=2, zorder=1))
    ax.text(stair_width + 7.5 + room_width / 2, F4R0 / 2, labelektro, ha='center', va='center', fontsize=12, zorder=2)

    ax.text(width / 2, height + 0.5, f" Floor {floor_number}", ha='center', fontsize=14, weight='bold', color='black', zorder=3)

# Function to draw the building with floor switching
def draw_building_with_switching(room_names=None):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.3)

    current_floor = [1]

    # Function to update the floor display
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

        # Set the axis limits and hide the axis
        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 7)
        ax.axis('off')
        plt.draw()

    # Function to switch between floors
    def switch_floor(delta):
        new_floor = current_floor[0] + delta
        if 1 <= new_floor <= 4:
            current_floor[0] = new_floor
            update_floor(current_floor[0])

    # Create buttons for navigation
    ax_prev = plt.axes([0.1, 0.05, 0.3, 0.075])
    ax_next = plt.axes([0.6, 0.05, 0.3, 0.075])
    btn_prev = Button(ax_prev, 'Previous Floor')
    btn_next = Button(ax_next, 'Next Floor')

    # Bind button actions
    btn_prev.on_clicked(lambda event: switch_floor(-1))
    btn_next.on_clicked(lambda event: switch_floor(1))

    # Customize button appearance
    for btn in [btn_prev, btn_next]:
        
        
        btn.label.set_fontsize(12)
        btn.label.set_color('black')
        btn.label.set_weight('bold')

    # Set the plot title
    plt.suptitle("Institut Teknologi Harapan Bangsa", fontsize=16, weight='bold', color='#2C3E50')

    # Display the first floor initially
    update_floor(current_floor[0])
    plt.show()

# Load room names from JSON file
room_names = load_room_names('room_names.json')

# Run the function to draw the building with floor switching
draw_building_with_switching(room_names=room_names)
