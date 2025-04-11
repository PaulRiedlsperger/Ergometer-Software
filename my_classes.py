from my_functions import estimate_max_hr, calculate_age
from datetime import date


class Person():
    """
    Superclass for all persons in the experiment.
    """
    def __init__(self, person : dict):
        self.name = person['name']
        self.surname = person['surname']

class Subject(Person):
    """
    Represents a test subject in an experiment.
    Inherits from Person and adds functionality to estimate maximum heart rate.
    """
    def __init__(self, person : dict):
   
        super().__init__(person)

        self.date_of_birth = person['age']
        self.age = calculate_age(self.date_of_birth)
        self.gender = person['gender']
    
    def estimate_maximum_hr(self):
        """
        Returns the estimated maximum heart rate of the subject and the date of birth based on the input dictionary.
        """
        self.estimate_max_hr = estimate_max_hr(self.age, self.gender)

        return self.estimate_max_hr, str(self.date_of_birth)
    
    # def __init__(self, person : dict):
    #     super().__init__(person)
    #     max_hr = estimate_max_hr(self.age, self.gender)
    #     print(f"Max HR: {max_hr}")
class Examiner(Person): 
    pass

class Experiment():
    def __init__(self, experiment : dict):
        self.experiment = experiment
    pass

person : dict = {"id": 1, "name": "Paul", "surname": "Doe", "age": date(2001,10,21), "gender": "male"}
print(Subject(person).estimate_maximum_hr())
