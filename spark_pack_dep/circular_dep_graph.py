import json
import networkx as nx
import matplotlib.pyplot as plt

# Path to your JSON file
input_file_path = r"C:\Users\Chanchal Vishwakarma\OneDrive\Documents\GitHub\Package_Dependency_Graph\packages_deps.json"  # Update this to your actual input file

# Read JSON data from the file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for item in data:
    print(item)# Limit printed output
         # Print selected items to keep track of progress

    try:
        name = item['Name']  # Access the 'Name' key
        deps = item['Deps']  # Access the 'Deps' key
    except KeyError as e:
        print(f"KeyError: {e} in item: {item}")  # Print the error and the problematic item
        continue  # Skip this item if there's a KeyError

    # Add the main package as a node
    # there are total of 13 packages depended on each other
    G.add_node(name)
    for dep in deps:
        G.add_node(dep)  # Add dependencies as nodes
        G.add_edge(name, dep)  # Create a directed edge from the package to its dependency

# Draw the graph
plt.figure(figsize=(15, 12))  # Increase figure size for clarity
pos = nx.spring_layout(G, k=0.5)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')  # Smaller nodes

# Draw edges
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=10, edge_color='gray')  # Adjusted edge size

# Draw labels with reduced font size
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # Smaller font size for labels

plt.title("Package Dependency Graph", fontsize=16)
plt.axis('off')  # Hide the axis
plt.tight_layout()  # Adjust layout to fit everything nicely
plt.show()  # Display the graph