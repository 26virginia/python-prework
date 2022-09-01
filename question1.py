#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_"+user_name)

user_name = input("Enter USERNAME: ")
hello_name(user_name)
