from pydantic import BaseModel


class Patient(BaseModel):
    name : str
    age : int


def inset_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

patient_info = {'name': 'sandeep', 'age': 20}

patient1 = Patient(**patient_info)

inset_patient_data(patient1)



