sztzring = "      Hello, World!     "
print(sztzring.strip())
sztzring = sztzring.strip()
print(sztzring.lower())
sztzring = sztzring.replace("World", "Python")
print(sztzring)
print(sztzring.count("o"))
print(sztzring.find("Python"))

print(sztzring.translate(str.maketrans("Helo", "1234")))