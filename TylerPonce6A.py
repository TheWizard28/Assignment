import re
#These will be the variables in authenticating the users input
pat1 = r'\d{3}d{3}-\d{d}'
pat2 = r'\d{3}\d{2}-\d{4}$'
pat3 = r'\d{5}'
print('Please enter your phone number, Social Security Number, or Zip Code')
#This will display examples to the user for what is required
print('Some examples are; 123-456-7890 for your phone number; 123-45-6789 for your SSN; and 12345 for your zip code')

#This is what will run the program
def verify_pat(pat1, pat2, pat3):
    s = input('Enter Phone, SSN, or Zip:')
#This is how the program will check the users input
    if re.match(pat1, s) or re.match(pat2, s) or re.match(pat3, s):
        print('Input is accepted')
    else:
        print('Input is Incorrect')
    return bool(s)
verify_pat(pat1, pat2, pat3)