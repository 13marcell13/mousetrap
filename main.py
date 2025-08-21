import pyautogui
import tkinter as tk

# Screen resolution
screen_resolution = pyautogui.size()

# GUI setup
root = tk.Tk()
root.title("MouseTrap")
root.geometry("400x50")
root.resizable(False, False)
root.attributes("-topmost", True)

label = tk.Label(root, text=f"Screen resolution: {screen_resolution.width}x{screen_resolution.height}\nMouse position: ")
label.pack()

# Add this after your label setup
close_button = tk.Button(root, text="✖", command=root.destroy, bg="#ff5555", fg="#ffffff", bd=0, font=("Segoe UI", 10, "bold"))
close_button.place(x=370, y=5, width=20, height=20)

# Function to update mouse position
def update_position():
    mouse_position = pyautogui.position()
    label.config(text=f"Screen resolution: {screen_resolution.width}x{screen_resolution.height}\nMouse position: {mouse_position.x}, {mouse_position.y}")
    root.after(100, update_position)  # schedule next update

# Start updating
update_position()

# Theme setup
root.attributes("-alpha", 0.8)
root.overrideredirect(True)
label.config(bg="#ffffff", fg="#000000")  # white-ish background
root.config(bg="#ffffff")  # same as label
label.pack(padx=10, pady=5)
label.config(font=("Segoe UI", 12, "bold"))

# Implementing window dragging
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    dx = event.x - root.x
    dy = event.y - root.y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")

label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", do_move)

root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

root.mainloop()
