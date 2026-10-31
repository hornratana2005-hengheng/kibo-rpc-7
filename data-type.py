# robot_name = "NRL Cosmic Explorer" #string
# age = 2 #integer
# height = 1.5 #float
# is_active = True #boolean
# warnings = None #NoneType



# print("Robot Name:", robot_name)
# print("Age:", age)
# print("Height:", height)
# print("Is Active:", is_active)
# print("Warnings:", warnings)


x_min, x_max = 8, 10 #tuple
pos_x = 9 #integer

is_safe = pos_x >= x_min and pos_x <= x_max #boolean
if is_safe == True:
    is_safe = "Safe"
else:
    is_safe = "Unsafe"

print("Within safe range:", is_safe)