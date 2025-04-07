from my_classes import Subject, Supervisor, Experiment

if __name__=="__main__":
    # Create a subject object
    subject = Subject({"id": 1, "first_name": "John", "last_name": "Doe", "sex": "male", "age": 30})
    
    # Create a supervisor object
    supervisor = Supervisor({"id": 2, "first_name": "Jane", "last_name": "Smith", "sex": "female", "age": 40})
    
    # Create an experiment object
    experiment = Experiment({"experiment_name": "Heart Rate Study", "date": "2023-10-01", 
                             "supervisor": supervisor, "subject": subject})
    # Print the objects to verify their creation

    print(subject.subject, supervisor.supervisor, experiment.experiment)