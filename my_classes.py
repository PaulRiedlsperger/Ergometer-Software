from my_functions import estimate_max_hr



class Person():
    def __init__(self, person_instance :dict):
        self.first_name = person_instance['first_name']
        self.last_name = person_instance['last_name']
        self.age = person_instance['age']
        self.sex = person_instance['sex']


class Subject(Person):
    def __init__(self, person_instance :dict):
        super().__init__(person_instance)
        self.estimate_max_hr = estimate_max_hr(self.age, self.sex)
        print(self.estimate_max_hr)

        
class Supervisor(Person):
    pass


person_instance : dict = {"id": 1, "first_name": "John", "last_name": "Doe", "sex": "male", "age": 30}

# class Experiment():
#     def __init__(self, experiment):
#         self.experiment = experiment 
#     pass         

Subject(person_instance)
