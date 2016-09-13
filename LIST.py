__author__ = 'Tomal- PC'

# LIST  : deals with complex data

# extra function is called by dot operator

movies = [ "The Holy Grail" ,  "The Life of Brian" , "The Meaning of Life" ]  # list, offset value 0,1,2  similar to array, no need of data types of movies
                                                                              # collections of objects


print(len(movies))  # how many data items on the list movies
print (movies[1])   # show the data having offset 1

print(movies)       # print all

#  append() extend() pop() functions(OR METHODS)

movies.append("dead pool")    # adding single object by calling (using dot) append() function to movies
print(movies)

movies.extend(["art of steel", " fury "])    # adding multiple objects by calling (using dot) extend() function to movies
print(movies)

movies.pop()  #removing a single object/data from movies
print(movies)


# remove() insert()  methods

movies.remove("The Meaning of Life")   # removing any desired data from the list
print(movies)

movies.insert(3,"the life of pie")    # adding a data at any position of the list insert(position , data)
print(movies)