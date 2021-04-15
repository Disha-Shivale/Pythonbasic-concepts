class User:
    def __init__(self,name,email,contact):
        self.name = name;
        self.email = email
        self.contact = contact

    def method1(demo):
        print("Your name is "+demo.name)

user = User("Disha","disha@gmail.com",9762616776)
del user.name   
user.method1()