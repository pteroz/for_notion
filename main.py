from source import *
from passwords import *

if __name__ == '__main__':
    gmail = gmail_work(USERNAME, PASSWORD, browser_off=False)
    gmail.change_names(NEW_FIRST_NAME, NEW_LAST_NAME)
    gmail.get_accounts_data()

    twitter = twitter_work(X_USERNAME, X_PASSWORD, browser_off=False)
    twitter.send_message('HELLO! TEST')
