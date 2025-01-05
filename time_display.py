import random
import time
import tkinter as tk

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