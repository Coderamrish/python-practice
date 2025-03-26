# lists
marks = [54, 45, 67, 76, 78]
print(marks[1:4])

list =[2,1,3]
list.append(4)
print(list)
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)
list.reverse()
print(list)
list.insert(1,5)
print(list)
list.remove(1)
print(list)
list.pop(2)
print(list)

# Tuples

# A built in data type that lets us create immutable sequences of values

tup = (2,1,3,4,5)
print(tup[2])
print(tup)

print(tup.index(2))
print(tup.count(2))

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []
mov1 = input("Enter the movies names: ")
mov2 = input("Enter the second movie: ")
mov3 = input("enter third name: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# WAP to check if a list contains a lapindrome of elements.

list1 = [2,2,2]
list2 = [2,2,4]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("plaindrome")
else:
    print("not palindrome")


# WAP to count the number of students with the "A" grade in the following tuple

grade = ("C", "D","A", "A","B", "B","A")
print(grade.count("A"))

# store the above values in a list & sort them from "A" to "D"

grade = ["C", "D","A", "A","B", "B","A"]
grade.sort()
print(grade)