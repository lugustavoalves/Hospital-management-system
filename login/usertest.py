from loginclass import LoginSystem

login_system = LoginSystem()

print(login_system.register_user("admin", "admin", "doctor"))

print(login_system.login_user("admin", "admin"))

# print(login_system.register_user("error", "error", "error"))
 
 