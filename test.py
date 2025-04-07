from my_classes import Subject, Supervisor, Experiment


if __name__ == "__main__":

    subject = Subject({"id": 1, "name": "Paul", "age": 25, "gender": "male"})
    supervisor = Supervisor({"id": 1, "name": "John"})
    experiment = Experiment({"id": 1, "name": "Experiment 1"})

    print(subject.subject, supervisor.supervisor, experiment.experiment)