import os
import sys
import json
from datetime import datetime

import requests as req
import matplotlib.pyplot as plt
from termcolor import colored

from functions import *

server = 'localhost:5000'

if len(sys.argv) < 2:
    print('Please provide init or submit as arguments')
    exit(1)

def get_stored_challenges():
    challenges = {}

    if os.path.isfile('./.ymir/challenges.json'):
        with open('./.ymir/challenges.json', 'r') as file:
            challenges = json.loads(file.read())

    return challenges

def run_functions(verbose = False):

    functions = {
        "challenge_1": challenge_1,
        "challenge_2": challenge_2,
        "challenge_3": challenge_3,
    }

    answer = {}

    challenges = get_stored_challenges()

    for function, challenge_id in zip(functions.keys(), challenges.keys()):
        if verbose: print(colored(challenges[challenge_id]['wording'], 'yellow'))
        for _input in challenges[challenge_id]['inputs']:

            _input_copy = _input.copy() if isinstance(_input, list) else _input
            
            output = functions[function](_input_copy)
            if verbose: print(f'input: {_input} : output: {output}')

            if challenge_id not in answer:
                answer[challenge_id] = []
            answer[challenge_id].append(output)
    
    return answer

if sys.argv[1] == 'init':
    try:
        response = req.get(f'http://{server}/challenge')
        if response.status_code == 200:
            parsed_response = response.json()
            if 'challenges' in parsed_response:
                challenges = parsed_response['challenges']
            
                print()

                index = 1
                for challenge in challenges.values():
                    print(colored(f"{index}. {challenge['wording']}", 'yellow'), '\n')
                    index += 1

        # Save file localy
        if not os.path.isdir('./.ymir'):
            os.mkdir('./.ymir')
        
        with open('./.ymir/challenges.json', 'w') as file:
            challenges['time-ini'] = datetime.timestamp(datetime.now())
            file.write(json.dumps(challenges))

    except Exception as e:
        print(str(e))

if sys.argv[1] == 'test':
    run_functions(verbose = True)

if sys.argv[1] == 'submit':
    challenges = get_stored_challenges()
    answers = run_functions()
    data = { 'answers': answers }

    response = req.post(f'http://{server}/challenge', json = data)
    if response.status_code == 200:
        parsed_response = response.json()['results']

        passed_all_tests = True
        challenge_index = 1

        for _id, test_results in parsed_response.items():
            print(colored(f"{challenge_index}. {challenges[_id]['wording']}", 'yellow'))
            test_index = 1
            for passed in test_results:
                if not passed:
                    passed_all_tests = False

                result = 'Passed' if passed else 'Failed'
                color = 'green' if passed else 'red'

                print(f"Test {test_index} : {colored(result, color)}")

                test_index += 1
            challenge_index += 1
        
        if passed_all_tests:
            time_ini = datetime.fromtimestamp(challenges['time-ini'])
            time_end = datetime.now()

            print(f'\nTTS: {time_end - time_ini}')

            # Submit time to server
            data = { 'entry': { str(datetime.now()): str(time_end - time_ini) }}
            response = req.post(f'http://{server}/time', json = data)
            if response.status_code == 201:
                print('Submited!')
            else:
                print(response.json()['message'])
    else:
        print(response.json())

if sys.argv[1] == 'history':
    response = req.get(f'http://{server}/time')
    if response.status_code == 200:
        parsed_response = response.json()
        if 'history' in parsed_response:
            for date, time in parsed_response['history'].items():
                date = date.split(' ')[0]
                time = time.split('.')[0]
                print(colored(f'{date} - {time}', 'yellow'))


if sys.argv[1] == 'new':
    template = '''# Your code goes here
def challenge_1(_input):
    pass

def challenge_2(_input):
    pass

def challenge_3(_input):
    pass
'''
    with open('./functions.py', 'w') as file:
        file.write(template)

