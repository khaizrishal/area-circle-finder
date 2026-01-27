import math
import tkinter as tk


def calculate_area():
    try: 
        pi = math.pi # All code made by Joel Robinson or ThatOneDev-studio
        dia = float(radius_entry.get()) * 2
        rad = dia / 2
        radtwo = rad * rad
        area = pi * radtwo
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    


# Create main window
root = tk.Tk()
root.title("Circle Area Finder")
root.geometry("400x200")

# Radius label and entry
tk.Label(root, text="Enter radius:").pack(pady=10)
radius_entry = tk.Entry(root)
radius_entry.pack()

# Calculate button

tk.Button(root, text="Calculate Area", command=calculate_area).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Area:")

result_label.pack(pady=10)

# Run app 
root.mainloop()




