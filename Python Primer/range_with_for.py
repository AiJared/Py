"""
We can use the range() method in for loops to iterate through a sequence of numbers. It can
be combined with the len() method to iterate through a sequence using indexing. Here is an
example.
"""

# list of genre
genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])


