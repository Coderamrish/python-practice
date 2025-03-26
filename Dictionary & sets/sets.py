collection = {1,2,3,4, "hello"}

print(collection)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

# store following word meanings in a python dictionary:

# table: "a piece of furniture", "list of facts & figures"
#cat: " a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", " list of facts & figures"]
}
print(dictionary)

# you are given a list of subjects for students . Assume one classroom is required for 1 subject. how many classrooms are needed by all students.

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}
print(subjects)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary  & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter phy: "))
marks.update({"phy" : x})

x = int(input(("enter math : ")))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)

# figure out a way to store 9 & 9.0 as separate values in the set.

values = {"9", 9.0}
print(values)

