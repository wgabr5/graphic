import matplotlib.pyplot as plt

def create_graph():
    # Sample data
    names = ['A', 'B', 'C', 'D', 'E']
    values = [5, 7, 3, 8, 6]

    # Create bar chart
    plt.bar(names, values)

    # Show the plot
    plt.show()

create_graph()