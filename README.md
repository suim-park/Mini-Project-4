![Multiple Python Versions](https://github.com/Suim-Park/Mini-Project-4/actions/workflows/main.yml/badge.svg)
# IDS-706-Data-Engineering :computer:

## Mini Project 4 :page_facing_up: 

## :ballot_box_with_check: Requirements
* Set up a `GitHub Actions workflow`</br>
* Test across at least `3 different Python versions`</br>

## :ballot_box_with_check: To-do List
* __Understanding GitHub Actions Matrix Build__: To understand the GitHub Actions Matrix Build and apply it by installing Multiple Python Versions.

## :ballot_box_with_check: Dataset
* `flights`
  - The data __flights__ is a DataFrame that is built in `seaborn` package. It's information about passengers in each month from 1949 to 1960.</br>
* `Brief Description`</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/8f899e92-13a7-4761-9d70-ae2e223ccd62.png" width="200" height="150"/></br>

## :ballot_box_with_check: In progress
__`Step 1`__ : Set up the environment to install multiple Python versions in GitHub Actions.
- `requirements.txt`: Add `matplotlib`(version=3.8.0) and `seaborn`(version=0.12.2) packages.</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/3a084460-3260-43c1-936a-14a56e898c82.png" width="160" height="180"/></br>
- `main.yml`: Build the multiple Python versions in __main.yml__ file. In this repository, since I used `matplotlib` packages that is not applied below 3.9 versions, I only added the Python versions above 3.9, which are `3.9`, `3.10.x`, and `3.11`.</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/340b494b-749c-4f93-89d4-3af324c4baae.png" width="400" height="700"/></br>
- `Makefile`</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/5c32a46b-6d6f-432b-a869-813684fd1bf8.png" width="470" height="330"/></br>
__`Step 2`__ : Create a main.py to see to briefly explore the dataset by creating a pivot table and draw a heat map to visualize the changes in the number of passengers by month and year. Test the functionality of main.py through test_main.py to ensure it is working correctly.</br>
* `main.py`</br>
```Python
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

    save_path = os.path.join(save_folder, "Heatmap of Flights Data.png")
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
```
* `test_main.py`</br>
```Python
# Test main.py
from main import load_data, describe_stat, pivot_table, draw_heat_map

def test_load_data():
    result_load_data = load_data()
    assert result_load_data is not None

def test_describe_stat():
    result_desc_stat = describe_stat()
    assert result_desc_stat is not None

def test_pivot_table():
    result_pivot_plot = pivot_table()
    assert result_pivot_plot is not None

def test_draw_heat_map():
    result_heat_map = draw_heat_map()
    assert result_heat_map is None

if __name__ == "__main__":
    test_load_data()
    test_describe_stat()
    test_pivot_table()
    test_draw_heat_map()
```
__`Step 3`__ : Verify if the table and plot are displayed correctly.
* Pivot table</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/32485ce0-7463-4442-9359-bec3136890b2.png" width="700" height="340"/></br>
* Visualization ([Heatmap of Flights Data.png](https://github.com/suim-park/Mini-Project-4/blob/main/Heatmap%20of%20Flights%20Data.png))</br>
<img src="https://github.com/suim-park/Mini-Project-4/assets/143478016/85dbcc34-6531-4ec9-ad98-7d000cfaa588.png" width="400" height="370"/></br>

__`Step 4`__ : Check whether GitHub Action has different multiple Python versions.</br>
* `GitHub Actions Matrix Build`</br>
![image](https://github.com/suim-park/Mini-Project-4/assets/143478016/d6665a7e-2548-423d-8d35-ae50b603cbb6)</br>
* `Makefile`: Check test, lint, and format at Codespace.</br>
<img src="https://github.com/suim-park/Mini-Project-3/assets/143478016/ae600810-c0d0-4828-9cfc-b42eb4d20179.png" width="600" height="300"/></br>
<img src="https://github.com/suim-park/Mini-Project-3/assets/143478016/49a08396-4666-4a46-8efc-c38ce41ae527.png" width="600" height="140"/></br>

## :ballot_box_with_check: Summary

__By verifying that the Python versions (3.9, 3.10, and 3.11) are built, I have confirmed that the GitHub Actions Matrix has been successfully set up.__</br>
