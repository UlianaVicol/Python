# IN: ligin, password
# FACT:
# OUT :message

# from databasename
SYS_LOGIN = "admin"
SYS_PASSW = "1234"

#from user input
login = input("login:")
passw = input("pass:")

#logic
hasaccess = SYS_LOGIN == login and SYS_PASSW == passw
if hasaccess:
    print("Access granted")
else:
    print("Access denied!")