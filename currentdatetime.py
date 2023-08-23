import tkinter as tk
import datetime

def show_date_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label.config(text="Current Date and Time: " + current_time)

# Create the main window
window = tk.Tk()
window.title("Date and Time Script")

# Create a label to display the date and time
label = tk.Label(window, text="Click the button to show the date and time", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Show Date and Time", font=("Arial", 12), command=show_date_time)
button.pack(pady=10)

# Run the main window event loop
window.mainloop()
stuff