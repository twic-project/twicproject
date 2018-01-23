'''
Useful links
https://pypi.python.org/pypi/python-firebase/1.2
https://temboo.com/python/parsing-json
'''

import json
import requests

CARD1 = '18004865AB9E'
CARD2 = '19007E5E4970'
FIREBASE_URL = 'https://twic-db.firebaseio.com'

def check_db(data, card_id, fingerprint):
    ''' This function checks the database for a valid card if and then looks up the corresponding fingerprint
     https://stackoverflow.com/questions/11700798/python-accessing-values-nested-within-dictionaries
     '''
    #data = get_data()
    # occurrence_of_card_id tracks if card id exists in the database
    # validateInput(data, card_id, fingerprint)
    occurrence_of_card_id = len(data)
    for item in data:
        occurrence_of_card_id = occurrence_of_card_id - 1
        if item['id'] != card_id:
            print('still searching for card id')
            continue
        else:
            print('card id found')
            occurrence_of_card_id = occurrence_of_card_id + 1
            if item['card_data']['fingerprint'] == fingerprint:
                print 'Success'
            else:
                print 'Invalid fingerprint'
    if occurrence_of_card_id == 0:
        print 'Card ID not found'

def get_data():
    '''
    Return data as a list of values
    Firebase automatically generates random ids (keys) that match up to values
    that we upload to the database, we do not need need to know what these keys are
    so we can just work with the values
    '''
    # Get data from firebase
    result = requests.get(FIREBASE_URL + '/test_data.json')
    # Convert data to json
    data = json.loads(result.text)
    return data.values()