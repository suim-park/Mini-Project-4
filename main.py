# Data Visulization
import matplotlib.pyplot as plt
import seaborn as sns

# Save File
import os


# Load the dataset and show the first five columns
def load_data():
    data = sns.load_dataset("flights")
    return data


# Calculate mean, median, standard deviation of each columns
def describe_stat():
    data_desc = load_data().describe()
    print(data_desc)
    return data_desc


# Create a pivot table
def pivot_table():
    pivot = load_data().pivot(index="month", columns="year", values="passengers")
    return pivot


# Draw a heat map and Save the .png File
def draw_heat_map():
    sns.heatmap(pivot_table(), cmap="YlGnBu")
    plt.title("Heatmap of Flights Data (Colored)", fontsize=20)

    directory_path = "C:/Users/suimp/OneDrive/Documents/"
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
    print(load_data())
    describe_stat()
    pivot_table()
    print(pivot_table())
    draw_heat_map()
