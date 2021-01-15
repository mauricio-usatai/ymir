from flask import Flask, request, jsonify

from services import ChallengeService
from services import TimeService

import json

app = Flask(__name__)

@app.route('/challenge', methods = ['GET'])
def get_challenges():
    response = {}

    try:
        cs = ChallengeService()
        challenges = cs.get_rand()

        response['challenges'] = challenges

        return jsonify(response)
    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500

@app.route('/challenge', methods = ['POST'])
def test_challenge():
    response = {}
    try :
        data = request.json

        cs = ChallengeService()
        results = cs.validate(data['answers'])

        response['results'] = results

        return jsonify(response)
    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500

@app.route('/time', methods = ['GET'])
def get_time_history():
    response = {}

    try:
        ts = TimeService()
        history = ts.get_history()

        response['history'] = history

        return jsonify(response)
    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500

@app.route('/time', methods = ['POST'])
def append_history():
    response = {}

    try:
        data = request.json
        entry = data['entry']

        ts = TimeService()
        ts.append_history(entry)

        response['success'] = True

        return jsonify(response), 201
    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500  

if __name__ == '__main__':
    app.run()
