import os
import pandas as pd
import numpy as np
from scipy import stats

# 1.0. Importing, merging, and relabeling the data.
os.chdir("C:/Users/kelop/OneDrive/Documents/GitHub/ReproRehab/")
os.listdir()

os.listdir("./data")
os.listdir("./data/EEG_sub_files/")

os.chdir("./data/EEG_sub_files/")

# Testing out importing data with 1 subject:
test = pd.read_csv("./oa01_ec.csv")

test.head()

file_names = os.listdir()
file_names
file_names[0]
file_names[6]

# A basic for-loop:
for i in range(1, 11):
    print(i)

for name in file_names:
    print(name)

k = 0
for file in file_names:
    k += 1
    print(file)
    print(k)


# Reading in the individual subjects and merging into a master file
if 1 <= 2:
    print("Oh yeah!")

# Evaluates to true, returns "Oh yeah!"

file_names[0]
if file_names[0] == "oa01_ec.csv":
    print("Oh yeah!")
    
# Evaluates to true, returns "Oh yeah!"

if file_names[0] == "OA01_ec.csv":
    print("Oh yeah!")

# Evaluates to false

if file_names[0] == "OA01_ec.csv":
    print("Oh yeah!")
else:
    print("Oh No!")
# Evaluates to false, returns "Oh No!"


# Putting an if-else statement inside our for-loop
for name in file_names:
    print(name)
    subject = pd.read_csv(name)

    # if the MASTER data set doesn't exist, create it
    if "MASTER" not in globals():
        MASTER = subject.copy()
        MASTER["file_id"] = name

    else:
        # Create the temporary data file:
        temp_dataset = subject.copy()
        temp_dataset["file_id"] = name

        MASTER = pd.concat([MASTER, temp_dataset])

        # Remove or "empty" the temporary data set
        del temp_dataset


MASTER.head()

# move the file ID and Hz columns to the front of the dataset
MASTER = MASTER[["file_id"] + [col for col in MASTER.columns if col != "file_id"]]

MASTER.head()

MASTER["file_id"].str.split("_", expand=True)[0]

MASTER["subID"] = MASTER["file_id"].str.split("_", expand=True)[0].map(str)
MASTER["condition"] = MASTER["file_id"].str.split("_", expand=True)[1].map(str)

MASTER["condition"].str[:2]

MASTER["condition"] = MASTER["condition"].str[:2].map(str)

MASTER.head()

MASTER = MASTER[["file_id", "subID", "condition"] + [col for col in MASTER.columns if col not in ["file_id", "subID", "condition"]]]

MASTER.head()

# Export the cleaned PSD data
os.getcwd()

os.chdir("C:/Users/kelop/OneDrive/Documents/GitHub/ReproRehab/data/")
MASTER.to_csv("MASTER_EO_and_EC_EEG.csv", index=False)
