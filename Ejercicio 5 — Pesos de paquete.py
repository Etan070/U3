weights = [12, 5, 20, 5, 8, 20, 5]

print("Count of 5:", weights.count(5))
print("First index of 20:", weights.index(20))

weights.remove(5)
weights.sort(reverse=True)

print("Modified list sorted descending:", weights)

# Output:
# Count of 5: 3
# First index of 20: 2
# Modified list sorted descending: [20, 20, 12, 8, 5, 5]