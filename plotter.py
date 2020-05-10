import random
import plotly.graph_objects as go

# Constants.
amber = [0, 1, 2, 3, 4]
flourite = [5, 6, 7]
damascus = [8]
amber_v = 3000
flourite_v = 6000
damascus_v = 6400
# Globals.
average_line = []
results = []
x_axis = []
total_g = 0
y = 0

while True:
    # User defined simulation count.
    print()
    try:
        sims = int(input("How many simulations? "))
    except ValueError:
        print()
        print('Invalid command.')
        continue
    # Simulation runs sims times.
    for y in range(1, sims + 1):
        print(f"Doing simulation {y}...")
        # Defining variables.
        a = 0
        f = 0
        d = 0
        x = 0

        # Checks 40 boxes.
        while x < 40:
            roll = random.randint(0, 99)
            if roll in amber:
                a += 1
            elif roll in flourite:
                f += 1
            elif roll in damascus:
                d += 1
            x += 1

        # Convert drops to money, report results.
        amber_g = a * amber_v
        flourite_g = f * flourite_v
        damascus_g = d * damascus_v
        g = amber_g + flourite_g + damascus_g
        total_g = total_g + g
        results.append(g)

    # Average of simulation, generates line co-ordinates.
    average_g = int(total_g / y)
    for x in range(1, sims + 1):
        average_line.append(average_g)

    # Generates x axis.
    for x in range(1, sims + 1):
        x_axis.append(x)

    # Begin generating plot.
    print()
    print("Generating plot...")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_axis, y=results, mode='markers', name='G'))
    fig.add_trace(go.Scatter(x=x_axis, y=average_line, mode='lines', name='Average'))
    fig.update_layout(
        title=f"Junk Heap Drop Simulation - {sims} times          Average: {average_g:,}G",
        xaxis_title="Simulation #",
        yaxis_title="G",
        font=dict(
            family="Tahoma, sans-serif",
            size=18,
            color="#000000"
        )
    )

    # Pushes plot.
    fig.show()

    # Print results.
    print()
    print(f"Average of {average_g:,}G from {y} simulations.")
    break
