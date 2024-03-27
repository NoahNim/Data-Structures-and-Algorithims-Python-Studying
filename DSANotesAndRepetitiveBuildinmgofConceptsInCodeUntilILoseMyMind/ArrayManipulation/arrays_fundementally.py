# UNDER THE HOOD:
# simple arrays are stored in memory in a contiguous manner
# static arrays are the simplest form of an array
#   - a static array means the array has a fixed size in memory allocatiom and can not be changed
#   - an array with 5 space allocations in memory that already has 3 elements can only have 2 more elements pushed into it, because memory after that 5th space may already have memory allocated to it
#   - you would have to make a new array that is a copy of the previous array with larger memory allocated to it
#   - so pushing into an array sometimes might not be O(1) but instead be O(n) because the new array must be genreated.
#   - however in terms of measuremnet it will often be considered O(1) to just push a new element of an array because most of the time it runs quickly at O(1) and there won't be a discernable difference but sometimes it is O(1), this is amortized time complexity

# ARRAY OPERATIONS | BIG-O TIME
# Read/Write Element | O(1)
# Insert/Remove End | O(1)
# Insert Middle or Beginning | O(n)
# Remove Middle or Beginning | O(n)

# Dynamic Arrays solve our space problem if we fill up the array with values and are the default for many languages
# A dynamic array is a random access, variable-size list data structure that allows elements to be added or removed
