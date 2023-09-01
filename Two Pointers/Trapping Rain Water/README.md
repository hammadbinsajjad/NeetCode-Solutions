# Trapping Rain Water

Create 2 arrays to store the max_left and max_right for each index and then take the minimum and subtract height of ith element from it. O(1) solution uses 2 pointers starting from left and right and moving the smallest while subtracting height of ith element from max_left or max_right whichever we moved