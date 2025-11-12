#
# try:
#     file= open("a_file.txt")
# except FileNotFoundError:
#     """when there is no such file"""
#     file= open("a_file.txt","w")
#
# else:
#     """if there is a file with no crashes"""
# finally:
#     """always """
#     """crashes code"""
#     raise KeyError("This is a self made error")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height must be greater than 3")
elif weight > 3:
    raise ValueError("Weight must be greater than 3")