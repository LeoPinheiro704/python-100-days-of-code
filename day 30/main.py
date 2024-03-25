
# try:
#   file = open("file.txt")
#   dictionary = {"key": "value"}
#   print(dictionary["dajshdjk"])
# except FileNotFoundError:
#   file = open("file.txt", "w")
#   file.write("Test")
# except KeyError as error_message:
#   print(f"The key {error_message} does not exist.")
# else:
#   content = file.read()
#   print(content)
# finally:
#   raise TypeError("This is an error that I made up.")
  # file.close()
  # print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human height should not be over 3 meters.3")

bmi = weight / height ** 2
print(bmi)