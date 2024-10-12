import pickle

# Example array
my_array = [1, 2, 3, 4, 5]

# Dump the array to a file
with open('array_file.pkl', 'wb') as f:
  pickle.dump(my_array, f)

# Load the array back from the file
with open('array_file.pkl', 'rb') as f:
  loaded_array = pickle.load(f)

print(loaded_array)  # Output: [1, 2, 3, 4, 5]
