import json
from helpers import pick_rand

from config.challenges import *

class ChallengeRepository:
    def get_random(self, n):
        try:
            with open(CHALLENGES_FILE, 'r') as file:
                challenges = json.loads(file.read())
                picked = pick_rand(challenges, n)
                return picked 
        except Exception as e:
            raise Exception(str(e))

    def get_by_id_list(self, ids):
        if len(ids) > 0:
            try:
                with open(CHALLENGES_FILE, 'r') as file:
                    challenges = json.loads(file.read())
                    challenges = { _id: challenges[_id] for _id in ids}  
                    return challenges
            except Exception as e:
                    raise Exception(str(e))
        else:
            return {}
