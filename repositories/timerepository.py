import json
import os
from config.challenges import *

class TimeRepository:
    def get_history(self):
        try:
            with open(TIME_HISTORY_FILE, 'r') as file:
                history = json.loads(file.read())
                return history
        except Exception as e:
            raise Exception(str(e))

    def append(self, entry):
        try:
            if os.path.exists(TIME_HISTORY_FILE):
                file = open(TIME_HISTORY_FILE, 'r+')
                contents = file.read()
                file.seek(0)
            
                if contents:
                    history = json.loads(contents)
                    key, value = list(entry.items())[0]
                    history[key] = value
                    file.write(json.dumps(history))
                else:
                    file.write(json.dumps(entry))

        except Exception as e:
            raise Exception(str(e))
            