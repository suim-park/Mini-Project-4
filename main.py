# Data Analysis
import pandas as pd
import numpy as np

# Data Visulization
import matplotlib.pyplot as plt
import seaborn as sns

# Save File
import os


# Load the dataset and show the first five columns
def load_data():
    data = pd.read_csv("flights.csv")
    data.head()
    return data


# Calculate mean, median, standard deviation of each columns
def describe_stat():
    data_desc = load_data().describe()
    print(data_desc)
    print()
    return data_desc


# Create a pivot table
def pivot_table():
    pivot_table = load_data().pivot(index="month", columns="year", values="passengers")
    pivot_table.head()
    return pivot_table


# Draw a heat map and Save the .png File
def draw_heat_map():
    ax = sns.heatmap(pivot_table(), cmap="YlGnBu")
    plt.title("Heatmap of Flight", fontsize=20)

    directory_path = "C:/Users/suimp/"
    folder_name = "Mini-Project-4"
    save_folder = os.path.join(directory_path, folder_name)

    # Make a directory if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    save_path = os.path.join(save_folder, f"Heatmap of Flights Data.png")
    plt.savefig(save_path)

    plt.show()
    return


if __name__ == "__main__":
    load_data()
    describe_stat()
    pivot_table()
    draw_heat_map()
