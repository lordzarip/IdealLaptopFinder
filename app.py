def suggest_laptop(os, primary_use, budget, processor, storage, ram, size):
    laptops = [
        {
            "name": "MacBook Air M1",
            "os": "macOS",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Apple M1",
            "storage": "256GB",
            "ram": "8GB",
            "size": "13-14 inches"
        },
        {
            "name": "MacBook Pro M2",
            "os": "macOS",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Apple M2",
            "storage": "512GB",
            "ram": "16GB",
            "size": "13-14 inches"
        },
        {
            "name": "Dell XPS 15",
            "os": "Windows",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Intel Core i7/i9",
            "storage": "1TB",
            "ram": "16GB or more",
            "size": "15-16 inches"
        },
        {
            "name": "Asus ROG Strix",
            "os": "Windows",
            "use_case": "Gaming",
            "budget": "Mid Range",
            "processor": "AMD Ryzen 7/9",
            "storage": "512GB",
            "ram": "16GB or more",
            "size": "15-16 inches"
        },
        {
            "name": "HP Pavilion",
            "os": "Windows",
            "use_case": "Casual",
            "budget": "Low Range",
            "processor": "Intel Core i3/i5",
            "storage": "256GB",
            "ram": "8GB",
            "size": "13-14 inches"
        },
        {
            "name": "Lenovo ThinkPad X1 Carbon",
            "os": "Windows",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Intel Core i7/i9",
            "storage": "1TB",
            "ram": "16GB or more",
            "size": "13-14 inches"
        },
        {
            "name": "Acer Predator Helios 300",
            "os": "Windows",
            "use_case": "Gaming",
            "budget": "Mid Range",
            "processor": "Intel Core i7/i9",
            "storage": "512GB",
            "ram": "16GB or more",
            "size": "15-16 inches"
        },
        {
            "name": "Microsoft Surface Laptop 4",
            "os": "Windows",
            "use_case": "Professional Work",
            "budget": "Mid Range",
            "processor": "AMD Ryzen 5",
            "storage": "512GB",
            "ram": "16GB",
            "size": "13-14 inches"
        },
        {
            "name": "Razer Blade 15",
            "os": "Windows",
            "use_case": "Gaming",
            "budget": "High-End",
            "processor": "Intel Core i7/i9",
            "storage": "1TB",
            "ram": "16GB or more",
            "size": "15-16 inches"
        },
        {
            "name": "Apple MacBook Pro 16",
            "os": "macOS",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Apple M1",
            "storage": "1TB",
            "ram": "16GB or more",
            "size": "15-16 inches"
        },
        {
            "name": "Dell Inspiron 14",
            "os": "Windows",
            "use_case": "Casual",
            "budget": "Low Range",
            "processor": "Intel Core i3/i5",
            "storage": "256GB",
            "ram": "8GB",
            "size": "13-14 inches"
        },
        {
            "name": "Lenovo IdeaPad Gaming 3",
            "os": "Windows",
            "use_case": "Gaming",
            "budget": "Low Range",
            "processor": "AMD Ryzen 5",
            "storage": "512GB",
            "ram": "8GB",
            "size": "15-16 inches"
        },
        {
            "name": "Asus ZenBook 14",
            "os": "Windows",
            "use_case": "Professional Work",
            "budget": "Mid Range",
            "processor": "Intel Core i5",
            "storage": "512GB",
            "ram": "16GB",
            "size": "13-14 inches"
        },
        {
            "name": "HP Spectre x360",
            "os": "Windows",
            "use_case": "Professional Work",
            "budget": "High-End",
            "processor": "Intel Core i7",
            "storage": "1TB",
            "ram": "16GB",
            "size": "13-14 inches"
        }
        # Add more laptop options based on requirements
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

# Get user input for each variable
os = input("Enter the operating system (macOS/Windows): ")
primary_use = input("Enter the primary use case (Gaming/Professional Work/Casual): ")
budget = input("Enter your budget (<RM2,500 (Low Range)/More than RM2,500 and less than RM4,500 (Mid Range)/>RM4,500 (High-End)): ")
processor = input("Enter the processor type (Intel Core i3/i5, AMD Ryzen 3/5, Intel Core i7/i9, AMD Ryzen 7/9, Apple M1 (for macOS only), Apple M2 (for macOS only)): ")
storage = input("Enter the storage (256GB/512GB/1TB): ")
ram = input("Enter the RAM (8GB/16GB or more): ")
size = input("Enter the size (13-14 inches/15-16 inches): ")

print(suggest_laptop(os, primary_use, budget, processor, storage, ram, size))
