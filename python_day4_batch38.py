# Removing white space.
name="      pavan        "
print(name)

name1="               pavan"
print(name1)


name2="pavan          "
print(name2)

name1.lstrip()
name2.rstrip()
name.strip()

students=["Divya","Latha","Surekha","Jyothi","Srusti","Monisha","likitha","bhavani"]
print(students)
print(students[1].title())
#joining method
students.append("Rishik")
print(students)
students.append("lakshmi")
print(students)

#insert method
students.insert(2,"suma")
print(students)

#modify method
students[4]="manasa"
print(students)

#deleting method
del students[9]
print(students)


