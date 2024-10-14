import json

# Function to detect circular dependencies using DFS
def find_circular_dependencies(packages):
    # Helper function to perform DFS
    def dfs(package, visited, rec_stack):
        visited.add(package)
        rec_stack.add(package)

        # Traverse dependencies of the current package
        for dep in package_dependencies.get(package, []):
            if dep not in visited:
                if dfs(dep, visited, rec_stack):
                    return True
            elif dep in rec_stack:
                return True  # Cycle detected

        rec_stack.remove(package)
        return False

    package_dependencies = {pkg['Name']: pkg['Deps'] for pkg in packages}
    visited = set()
    rec_stack = set()

    # Check each package for circular dependencies
    circular_packages = []
    for package in package_dependencies:
        if package not in visited:
            if dfs(package, visited, rec_stack):
                circular_packages.append(package)

    return circular_packages


# Load package data from the given file path
json_file_path = r"C:\Users\Chanchal Vishwakarma\OneDrive\Documents\GitHub\Package_Dep\output_list.json"
with open(json_file_path, 'r') as file:
    packages = json.load(file)

# Find packages with circular dependencies
circular_packages = find_circular_dependencies(packages)

if circular_packages:
    print("Packages with circular dependencies found:")
    for pkg in circular_packages:
        print(pkg)
else:
    print("No circular dependencies found.")
