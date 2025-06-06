from pydantic import BaseModel
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str
    age : int
    weight : float = False
    married: Optional[bool] = None
    allergiers: Optional[list[str]]  = None
    contact_details: Optional[Dict[str, str]] = None



patient_info = {'name': 'sandeep', 
                'age': 20, 
                'weight': 66.5, 
             #   'married': False, 
                'allergiers':['pollen', 'dust'], 
                'contact_details':{'email':'abc@gmail.com', 'phone': '974392849593'}}


def inset_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergiers)

patient1 = Patient(**patient_info)

inset_patient_data(patient1)



