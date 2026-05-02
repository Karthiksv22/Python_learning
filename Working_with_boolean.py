print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))


email = ""
phone = "234234324234"
username = ""
# Allows registration 
# if any feild is filled
print(any([email,phone,username]))                 # This prints true only either of three values one should have value then it will print true

# Allows registration 
# only of all feilds is filled
print(all([email,phone,username]))                 # this prints true only when all the values are there or else even if one is missing it will print false


# Operators

print(10 == 10)
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print(7 <= 7)

print(3 < 4 < 6)               # Chain comparison where it compare all values should be true

# Logical Operators

print(3 > 1 and 5 < 1)                  # and operator used here
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)                   # Or operator used here
print(3 < 1 or 5 < 1)

print(not 3 > 2)
print(not True)                         # not operator is used here where true is flipped to false and false is flipped to true
print(not False)
print(not not False)

# Allow access only if  the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)

# Membership operator

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

# Identity operators

x = ['a', 'b','c']
y = ['a', 'b','c']                            

print(x==y)                  # This depends on memory allocation in the backend 
print(x is y)

x = 10
y = 10

print(x==y)                   # This depends on memory allocation in the backend 
print(x is y)


