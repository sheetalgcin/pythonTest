#get user email address

email = input("What is your email address?: ").strip()

#slice user name

user = email[:email.index("@")]

#domain name

domain = email[email.index("@") + 1 :]

#format message

output = "My user name is {} domain is {}".format(user,domain)

#display output message

print(output)
