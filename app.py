import tkinter as tk
from tkinter import ttk, messagebox

def suggest_laptop(os, primary_use, budget, processor, storage, ram, size):
    laptops = [
        {"name": "MacBook Air M1", "os": "macOS", "use_case": "Professional Work", "budget": "High-End", "processor": "Apple M1", "storage": "256GB", "ram": "8GB", "size": "13-14 inches"},
        {"name": "MacBook Pro M2", "os": "macOS", "use_case": "Professional Work", "budget": "High-End", "processor": "Apple M2", "storage": "512GB", "ram": "16GB", "size": "13-14 inches"},
        {"name": "Dell XPS 15", "os": "Windows", "use_case": "Professional Work", "budget": "High-End", "processor": "Intel Core i7/i9", "storage": "1TB", "ram": "16GB or more", "size": "15-16 inches"},
        {"name": "Asus ROG Strix", "os": "Windows", "use_case": "Gaming", "budget": "Mid Range", "processor": "AMD Ryzen 7/9", "storage": "512GB", "ram": "16GB or more", "size": "15-16 inches"},
        {"name": "HP Pavilion", "os": "Windows", "use_case": "Casual", "budget": "Low Range", "processor": "Intel Core i3/i5", "storage": "256GB", "ram": "8GB", "size": "13-14 inches"},
        {"name": "Lenovo ThinkPad X1 Carbon", "os": "Windows", "use_case": "Professional Work", "budget": "High-End", "processor": "Intel Core i7/i9", "storage": "1TB", "ram": "16GB or more", "size": "13-14 inches"},
        {"name": "Acer Predator Helios 300", "os": "Windows", "use_case": "Gaming", "budget": "Mid Range", "processor": "Intel Core i7/i9", "storage": "512GB", "ram": "16GB or more", "size": "15-16 inches"},
        {"name": "Microsoft Surface Laptop 4", "os": "Windows", "use_case": "Professional Work", "budget": "Mid Range", "processor": "AMD Ryzen 5", "storage": "512GB", "ram": "16GB", "size": "13-14 inches"},
        {"name": "Razer Blade 15", "os": "Windows", "use_case": "Gaming", "budget": "High-End", "processor": "Intel Core i7/i9", "storage": "1TB", "ram": "16GB or more", "size": "15-16 inches"},
        {"name": "Apple MacBook Pro 16", "os": "macOS", "use_case": "Professional Work", "budget": "High-End", "processor": "Apple M1", "storage": "1TB", "ram": "16GB or more", "size": "15-16 inches"},
        {"name": "Dell Inspiron 14", "os": "Windows", "use_case": "Casual", "budget": "Low Range", "processor": "Intel Core i3/i5", "storage": "256GB", "ram": "8GB", "size": "13-14 inches"},
        {"name": "Lenovo IdeaPad Gaming 3", "os": "Windows", "use_case": "Gaming", "budget": "Low Range", "processor": "AMD Ryzen 5", "storage": "512GB", "ram": "8GB", "size": "15-16 inches"},
        {"name": "Asus ZenBook 14", "os": "Windows", "use_case": "Professional Work", "budget": "Mid Range", "processor": "Intel Core i5", "storage": "512GB", "ram": "16GB", "size": "13-14 inches"},
        {"name": "HP Spectre x360", "os": "Windows", "use_case": "Professional Work", "budget": "High-End", "processor": "Intel Core i7", "storage": "1TB", "ram": "16GB", "size": "13-14 inches"},
    ]
    
    suggestions = []
    for laptop in laptops:
        if (laptop["os"] == os and
            laptop["use_case"] == primary_use and
            laptop["budget"] == budget and
            laptop["processor"] == processor and
            laptop["storage"] == storage and
            laptop["ram"] == ram and
            laptop["size"] == size):
            suggestions.append(laptop["name"])
    
    if suggestions:
        return f"Based on your criteria, we suggest: {', '.join(suggestions)}"
    else:
        return "No laptop matches your criteria. Please adjust your preferences and try again."

def get_laptop_suggestion():
    os = os_var.get()
    primary_use = use_case_var.get()
    budget = budget_var.get()
    processor = processor_var.get()
    storage = storage_var.get()
    ram = ram_var.get()
    size = size_var.get()
    
    suggestion = suggest_laptop(os, primary_use, budget, processor, storage, ram, size)
    messagebox.showinfo("Laptop Suggestion", suggestion)

# Create the main window
root = tk.Tk()
root.title("Laptop Suggestion Tool")

# Define variables
os_var = tk.StringVar()
use_case_var = tk.StringVar()
budget_var = tk.StringVar()
processor_var = tk.StringVar()
storage_var = tk.StringVar()
ram_var = tk.StringVar()
size_var = tk.StringVar()

# Create and place widgets
ttk.Label(root, text="Operating System:").grid(row=0, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=os_var, values=["macOS", "Windows"]).grid(row=0, column=1)

ttk.Label(root, text="Primary Use Case:").grid(row=1, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=use_case_var, values=["Gaming", "Professional Work", "Casual"]).grid(row=1, column=1)

ttk.Label(root, text="Budget:").grid(row=2, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=budget_var, values=["<RM2,500 (Low Range)", "More than RM2,500 and less than RM4,500 (Mid Range)", ">RM4,500 (High-End)"]).grid(row=2, column=1)

ttk.Label(root, text="Processor Type:").grid(row=3, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=processor_var, values=["Intel Core i3/i5", "AMD Ryzen 3/5", "Intel Core i7/i9", "AMD Ryzen 7/9", "Apple M1 (for macOS only)", "Apple M2 (for macOS only)"]).grid(row=3, column=1)

ttk.Label(root, text="Storage:").grid(row=4, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=storage_var, values=["256GB", "512GB", "1TB"]).grid(row=4, column=1)

ttk.Label(root, text="RAM:").grid(row=5, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=ram_var, values=["8GB", "16GB or more"]).grid(row=5, column=1)

ttk.Label(root, text="Size:").grid(row=6, column=0, sticky=tk.W)
ttk.Combobox(root, textvariable=size_var, values=["13-14 inches", "15-16 inches"]).grid(row=6, column=1)

ttk.Button(root, text="Get Suggestion", command=get_laptop_suggestion).grid(row=7, columnspan=2)

# Run the main loop
root.mainloop()
