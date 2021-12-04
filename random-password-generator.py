import string,random
 
# generate password
def generatePassword(length):
    new_password= "".join(random.sample(password,length))
    return new_password

# establishing min requirement
min_length= 8
pass_length= input(' please enter password length: ')

# defining patterns
lower= string.ascii_lowercase
upper= string.ascii_uppercase
digits= string.digits
symbols= string.punctuation
password= lower+digits+upper+symbols

# check password length
while True:
    try:
        pass_length= int(pass_length)
        if pass_length >= min_length:
            break
        else: 
            pass_length= int(input(' Please enter a valid password length. 8 is the min:  '))

    except ValueError:
        print('only numbers are allowed!')
        pass_length= input('Please enter a valid number of characters: ')
    except ValueError:
        print(int(input('Please try again: ')))
    
new_password= generatePassword(pass_length)
print('your new password is: ', new_password)