from my_functions import estimate_max_hr, calculate_age, post
from datetime import date
import requests
import json


class Person():
    """
    Superclass for all persons in the experiment.
    """
    def __init__(self, person : dict):
        self.name = person['name']
        self.surname = person['surname']
        self.id = person['id']

    def post(self):
        person_json = json.dumps(self.__dict__)
        print("JSON: ", person_json)

        ## Creata a new person
        # Define the URL of the API
        url = "http://127.0.0.1:5000/person"

        # Define the data you want to send

        data = {
            "name": self.name,
            "surname": self.surname,
            "id": self.id
        }

        # Convert the data to JSON format
        data_json = json.dumps(data)

        # Send a POST request to the API
        response = requests.post(url, data=data_json)

        # Print the response from the server
        print(response.headers['Location'])
        print(response.text)

    

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

person : dict = {"id": 1, "name": "Paul", "surname": "Doe", "age": date(2001,10,21), "gender": "male", "id": 1}
#print(Subject(person).estimate_maximum_hr())
apiperson = Person(person)
Person.post(apiperson)