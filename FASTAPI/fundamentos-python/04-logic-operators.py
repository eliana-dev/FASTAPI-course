# and
age = 25
licensed = False

if age >= 18 and licensed:
    print("u can drive")
else:
    print("u cant drive sis")


# or

is_student = False
membership = True

if is_student or membership:
    print("you'll get a special price!")

# not
is_admin = False
if not is_admin:
    print("you are not an admin.")
else:
    print("Welcome")


# short circuiting
name = "eliana"
print(name and name.upper())
