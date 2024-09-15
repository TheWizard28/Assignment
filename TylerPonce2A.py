#This program will scan emails to detect for spam risk
#This will be the list of keywords to look for
def is_spam_phrases_index(spam_words):
    spam_words = ['act now','urgent','free','earn money','click here','buy now','limited time offer','get rich quick','make money now','earn extra cash','guaranteed',
                  'winner','bonus','winner','act now','while supplies last','risk free','great offer','click bellow','click here,','drastically reduced','sign up free today',
                  'order today','apply now','special promotion','fantastic deal','satisfaction guaranteed','free quote','no strings attached','cards accepted',]

#These will be the variables for searching and counting the number of spam words
spam_str = spam_words
email = spam_str.count(spam_words)
spam_num = -1

while True: #This is where the user will enter their email
        question = input("Please enter your email (type 'n' to exit);")
        spam_num = email_str.find(spam_str, spam_num + 1)
        #This section will note the levels of risk in the email
        if spam_num <5:
            print('Low risk of Spam detected')

        if spam_num  >10 <20:
            print("Moderate risk of Spam detected")

        if spam_num >20:
            print('High risk of Spam detected')

        if question.lower() == 'n':
            print('Thank you for your time')
            break#Will allow user to exit program if they are finished


