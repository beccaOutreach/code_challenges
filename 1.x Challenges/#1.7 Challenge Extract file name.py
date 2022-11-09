filelabelname = input("What is your file called? ")
fs = filelabelname.split(".")

print(("Your file type is: ") + repr(fs[-1]))