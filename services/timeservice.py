from repositories import TimeRepository

class TimeService:
    def __init__(self):
        self.repo = TimeRepository()

    def get_history(self):
        try:
            history = self.repo.get_history()
            return history
        except Exception as e:
            raise Exception(str(e))

    def append_history(self, entry):
        try:
            self.repo.append(entry)
        except Exception as e:
            raise Exception(str(e))


