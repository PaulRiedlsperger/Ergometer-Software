from my_functions import estimate_max_hr

class Subject():
    def __init__(self, subject : dict):
        self.subject = subject
        self.max_hr = estimate_max_hr(subject['age'], subject['gender'])
        print(self.max_hr)



class Supervisor():
    def __init__(self, supervisor : dict):
        self.supervisor = supervisor
    pass


class Experiment():
    def __init__(self, experiment : dict):
        self.experiment = experiment
    pass

Subject({"id": 1, "name": "Paul", "age": 25, "gender": "male"})
