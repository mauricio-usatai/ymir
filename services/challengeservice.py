from repositories import ChallengeRepository
from solutions import *
from config.challenges import *

class ChallengeService:
    def __init__(self):
        self.repo = ChallengeRepository()

    def get_rand(self):
        challenges_dict = self.repo.get_random(CHALLENGES_NUM)
        for value in challenges_dict.values():
            del value['function']
        
        return challenges_dict

    def validate(self, answers):
        results = {}

        ids = [_id for _id in answers.keys()]
        challenges = self.repo.get_by_id_list(ids)

        for _id in ids:
            results[_id] = []
            for _input, submited_answer in zip(challenges[_id]['inputs'], answers[_id]):
                # Call answer functions
                correct_answer = None
                if isinstance(_input, str):
                    correct_answer = eval(f"{challenges[_id]['function']}('{_input}')")
                else:
                    correct_answer = eval(f"{challenges[_id]['function']}({_input})")

                if submited_answer == correct_answer:
                    results[_id].append(True)
                else:
                    results[_id].append(False)
        return results