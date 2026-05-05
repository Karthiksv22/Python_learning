
# If conditon code
score = 100
if score >= 90 :
  print("A")

# if else condition code
score = 50
if score >= 90 :
  print("A")
else:
  print("B")

# if elif and else condition code
score = 50
if score >= 90 :
  print("A")
elif score >= 80:
  print("B")
else:
  print("C")

# if elif and one more elif and else condition code
score = 50
if score >= 90 :
  print("A")
elif score >= 80:
  print("B")
elif score >= 80:
  print("C")
else:
  print("D")

# Conditional and logical Operators
score = 50
submitted_project = True
if score >= 90 and submitted_project :
  print("A+")
elif score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 80:
  print("C")
else:
  print("D")

# Inline if (Ternary is used)
# Only used for simple logic
  
print("A" if score >= 90 else "F")

# Match case # Nothing but switch case

country = "Egypt"
if country == "United states":
  print("US")
elif country == "India":
  print("IN")
elif country == "Egypt":
  print("EG")
elif country == "Germany":
  print("DE")
else:
  print("Unknown country")

# Rather than using if elif u can use this match 
match country:
  case "United states":
   print("US")
  case "India":
   print("IN")
  case "Egypt":
   print("EG")
  case "Germany":
   print("DE")
  case _:
   print("Unknown country")

# Challenge vedio of conditional statement
email = "" 
email = email.strip()
if email == "":
  print("Email cannot be empty")
elif not('.' in email and 'a' in email):
  print("Email must contain . and a")
elif email.count('@') != 1:
  print("Must exactly contain one @")
elif email.endswith('.com') or email.endswith('.org') or email.endswith('.net'):
  print("Must end with .com , .org , .net")
elif len(email) > 254:
  print("Not be more than 254")
else:
  print("Email is valid")



