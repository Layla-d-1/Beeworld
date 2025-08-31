# Student Name: Layla Dawood
# Student ID:23100624
#
# beeworld.py - simulation of bee colony in a world with trees and flowers
#
# Version information: 2
#
# Usage: There are two modes to use to run the program:
# Interactive mode: Run scrpit in terminal using python: python3 beeworld.py -i ( will be asked for user input of number of bees and simulation length
# Batch mode: open terminal and run the script with the csv file as an argument using; python3 beeworld.py -p params.csv.
#
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from buzzness import Bee, Flower, Frame
import argparse
import csv
import sys

# Default hive & flower setup
hive_pos = (5, 5)
flower_positions = [(5, 5), (2, 2), (7, 7)]

# Main Simulation Function 
def run_simulation(bees, hive_pos, frame, sim_length):
    hive_storage = 0
    flowers = [Flower(pos=p, nectar=2) for p in flower_positions]

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

    for step in range(sim_length):
        print(f"\n--- Step {step} ---")
        bee_x = []
        bee_y = []

        for bee in bees:
            result = bee.step_change()
            x, y = bee.get_pos()

            if bee.carrying:
                print(f"Bee {bee.ID} is carrying nectar, current pos: {x, y}")

            if result == 'delivered':
                hive_storage += 1
                frame.add_honey()
                print(f"Bee {bee.ID} delivered nectar to hive! Total stored: {hive_storage}")

            for flower in flowers:
                if flower.get_pos() == (x, y) and flower.has_nectar() and not bee.carrying:
                    flower.collect_nectar()
                    bee.carrying = True
                    print(f"Bee {bee.ID} collected nectar at {x, y} and is returning to hive")

            bee_x.append(x)
            bee_y.append(y)

        ax.clear()
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')

        # Plot hive
        hx, hy = hive_pos
        ax.scatter(hx, hy, color='brown', marker='s', s=200)
        ax.text(hx, hy - 0.5, f"Honey: {hive_storage}", ha='center', fontsize=10)

        # Plot flowers
        for flower in flowers:
            fx, fy = flower.get_pos()
            color = 'magenta' if flower.has_nectar() else 'gray'
            ax.scatter(fx, fy, color=color, marker='*', s=200)
            print(f"[DEBUG] Flower at {fx, fy}, nectar={flower.nectar}")

        # Plot bees
        ax.scatter(bee_x, bee_y, color='yellow', s=100)

        # Plot honeycomb (frame)
        cell_data = frame.get_cells()
        ax.imshow(cell_data, cmap='YlOrBr', extent=(6, 11, 0, 5), origin='lower')

        plt.pause(0.3)

    plt.ioff()
    plt.show()
    input("Press Enter to exit...")

# Input Handling
def interactive_mode():
    print("Running in INTERACTIVE mode.")
    num_bees = int(input("Enter number of bees: "))
    sim_length = int(input("Enter simulation length: "))
    return num_bees, sim_length

def load_parameters_from_file(filename):
    print(f"Loading parameters from {filename}...")
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        print("Read rows:", rows)  # Debug line
        bees = int(rows[0][1])  # bees,5
        steps = int(rows[1][1]) # steps,40
    return bees, steps

#Program Entry Point 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true", help="Run in interactive mode")
    parser.add_argument("-p", metavar="paramfile", help="Run in batch mode with parameter file")
    args = parser.parse_args()

    if args.i:
        NUM_BEES, SIM_LENGTH = interactive_mode()
    elif args.p:
        NUM_BEES, SIM_LENGTH = load_parameters_from_file(args.p)
    else:
        print("Please use -i for interactive or -p <file> for batch mode.")
        sys.exit(1)

    bees = [Bee(ID=i, pos=hive_pos) for i in range(NUM_BEES)]
    frame = Frame()
    run_simulation(bees, hive_pos, frame, SIM_LENGTH)
