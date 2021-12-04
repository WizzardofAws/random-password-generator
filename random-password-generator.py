import string,random

# defining patterns
lower= string.ascii_lowercase
upper= string.ascii_uppercase
digits= string.digits
symbols= string.punctuation

# while loop for checking password length, handling exceptions
while True:
    try:
        pass_length= int(input(' Please enter length of password (min is 8 characters):  '))
        if len(pass_length) >= 8:
            break
        else: 
            int(input(' Please enter a valid password length. Passwords must be 8 characters or more: '))

    except ValueError:
        print('only numbers are allowed!')
        int(input('Please enter a valid number of characters: '))

password= lower+digits+upper+symbols

# this will return a list. joined:
def shufflePassword(password):
     new_password= "".join(random.sample(password,pass_length))
print(new_password)
