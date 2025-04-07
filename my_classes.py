from my_functions import estimate_max_hr

class Subject():
    def __init__(self, subject):
        self.subject = subject
        self.estimate_max_hr = estimate_max_hr(subject['age'], subject['sex'])

        print(self.estimate_max_hr)	

    
class Supervisor():
    def __init__(self, supervisor):
        self.supervisor = supervisor
    pass    


class Experiment():
    def __init__(self, experiment):
        self.experiment = experiment 
    pass         


Subject({"id": 1, "first_name": "John", "last_name": "Doe", "sex": "male", "age": 30})