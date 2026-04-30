# Types
name = "Baraa"
print(type(name))

age = 24
print(type(age))
print("Your Age is:" + str(age))
age = age + 4
age = str(age)
print(type(age))

# String Operators  Math

password = "  123a"              # len even if u give space also it will be counted.
print(len(password))

if len(password) < 8:
    print("Your password is too short!")


# Math
text = """
Python is easy to learn
Python is powerful
Many people love python
"""

print(text.count("Python"))         # This .count helps to count characters


# Replace method
phone = "36-492-6422"
print(phone.replace("-",""))


# Challenge for replace method

phone = "+49 (176) 123-4567"                                                #Challenge completed f
print(phone.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ",""))
# f-Strings
name = "Sam"
age = 34
is_student = False
print("My name is "+name+", I am " + str(age) + "years old, and student status is "+ str(is_student)+".")

# using f-Strings
print(f"My name is {name} I am {age} years old, and student status is {is_student}.")

# Transformation split method
stamp = "2026-09-20 14:30"
print(stamp.split(" "))
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))


# Indexing and slicing
# 1. Indexing

text = 'Python'
# Extract the first character
print(text[0])            # P
print(text[-6])           # P

#Extract the last character
print(text[5])          # n
print(text[-1])         # n

# Extract t
print(text[2])
print(text[-4])

# 2. Slicing
date = "2026-09-20"

#Extract the year
print(date[0:4])

#Extract the month
print(date[5:7])

# Extract date
print(date[8:])
print(date[-2:])



# Removing spaces
text = "  Engineering".lstrip()             # Use it for left side if there is spaces
print(text)

text = "Engineering  ".rstrip()             # Use it for right side if there is spaces
print(text)

text = "  Engineering  ".strip()            # Use it for if both the sides if there is space
print(text)

text = " Engineering"
print(len(text))
print(len(text.strip()))

# Upper and lower case
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

# Case Conversion
search = " Email".lower().strip()
data = "email".lower().strip()

print(search == data)


# Searching
# starts with
phone = "+48-176-12345"
print(phone.startswith("+48"))

# endswith
email = "baraaoutlook.com"
print(email.endswith(".com"))

#in 
print("@" in email)

#find
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[phone1.find("-")+1:])

#Validation string values and numbers

country = "USA"
print(country.isalpha())

phone = "236493269362"
print(phone.isnumeric())








