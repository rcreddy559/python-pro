user_profile = {
    "name": "None",
    "age": 0,
    "email": "None",
    "is_active": True,
    "location": "None",
}

ravi_profile = {
    "name": "Ravi",
    "age": 30,
    "email": "rc.reddy@zohomail.in",
    "is_active": True,
}

profile =   user_profile | ravi_profile
print("User Profile: ", user_profile)
print("Ravi Profile: ", ravi_profile)
print("Combined Profile: ", profile)
