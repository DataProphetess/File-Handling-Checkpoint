
# # File Handling: File Handling Checkpoint
import numpy as np

with open("Loan_prediction_dataset.csv", "r") as f:
        data = f.read()

data = np.genfromtxt("Loan_prediction_dataset.csv", delimiter=",", usecols=8, filling_values=0)

# ## creating a 1D array
array = np.array(data)

# #calculating the mean, median and standard deviation of the loan_amount arraymean = np.mean(array)print(f"The mean is: {mean}")

median = np.median(array)

print(f"\nThe median is: {median}")

std = np.std(array)

print(f"\nThe std is: {std}")

max = np.max(array)

print(f"\nThe max is: {max}")

min = np.min(array)

print(f"\nThe min is: {min}")

var = np.var(array)

print(f"\nThe Varience is: {var}")