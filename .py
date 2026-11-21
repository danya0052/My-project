with open(".py", "a", encoding-"utf-8" ) as file:
    file.write("\ntest")
    
with open(".py", "r", encoding-"utf-8" ) as file:
    content = file.read()
    print(content)