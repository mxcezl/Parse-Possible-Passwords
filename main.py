from utils.regex import PasswordMatcher
from utils.http import getRawResponse
import configparser

# Configuration part
config = configparser.ConfigParser()
config.read('application.ini')
SEPARATOR = '|'

combolist = getRawResponse(config['DEFAULT']['URL_TO_SCRAPE'])
matcher = PasswordMatcher(6, 10)

counter = 0
for combo in combolist.split():
    combo = str(combo, 'utf-8')
    if SEPARATOR in combo:
        email, password = combo.split(SEPARATOR)
        if matcher.isPasswordValid(password):
            print('[+] You should try this combo : {}'.format(combo))
            counter += 1
print('\n=> Analysed {} combo(s) !'.format(counter))