def linear_search(arr, target):
     for i in range(len(arr)):
          if arr[i] == target:
               return i  # Return index of target element if found in the array
     return -1 # Return -1 if element not found in the array

# Example usage:
my_array = [10, 23, 5, 2, 15, 7, 30]
target_element = 16

result = linear_search(my_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")