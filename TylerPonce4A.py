import time

time.sleep(5)
#This program will scan emails to detect for spam risk and also time the program
#This will be the list of keywords to look for
def check_spam():
    def make_timer(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            ret_val = func(*args, **kwargs)
            t2 = time.time()
            print('Time elapsed was', t2 - t1)
            return ret_val

        return wrapper
    #This is the spam list to reference
    spam_words = ['act now', 'urgent', 'free', 'earn money', 'click here', 'buy now', 'limited time offer', 'get rich quick', 'make money now', 'earn extra cash', 'guaranteed',
                  'winner','bonus','winner','act now','while supplies last','risk free','great offer','click bellow','click here,','drastically reduced','sign up free today',
                  'order today','apply now','special promotion','fantastic deal','satisfaction guaranteed','free quote','no strings attached','cards accepted']

    #This is where the user will input their email
    email = input('Please enter your email')

    #This will be the counter
    spam_num = 0

    for words in spam_words:
        if words.lower() in email.lower():
            spam_num += 1

    if spam_num <= 5:
        print('Low risk of Spam detected')

    elif 5 < spam_num <= 20:
        print("Moderate risk of Spam detected")

    else:
        print('High risk of Spam detected')


    print(f'Your spam score is {spam_num}')
    print('Thank you for your time')


check_spam()
