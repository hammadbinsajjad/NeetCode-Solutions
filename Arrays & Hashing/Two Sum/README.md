# TWO SUM

###### Solution 1

Using 2 pointers on the sorted dictionary, if sum is greater move the right one back else move left one forward. Return the indices when sum is found

###### Solution 2 (Better)

Create a dictionary to hold values and their indices and find if after subtracting the current num from target we can find the number in the dictionary. If we can we return the current index and from the dictionary. Otherwise we add the current value and its index in the dictionary.