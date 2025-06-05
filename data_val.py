from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    linked_url: AnyUrl
    weight : float = False
    married: Optional[bool] = None
    allergiers: Optional[list[str]]  = None
    contact_details: Optional[Dict[str, str]] = None



patient_info = {'name': 'sandeep', 
                'age': 20, 
                'weight': 66.5, 
                'married': False, 
                'allergiers':['pollen', 'dust'], 
                'contact_details':{'phone': '974392849593'},
                'email': 'abc@gmail.com',
                'linked_url':'http://linkedin.com/1234'
                }


def inset_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergiers)
    print(patient.email)
    print(patient.linked_url)

patient1 = Patient(**patient_info)

inset_patient_data(patient1)



