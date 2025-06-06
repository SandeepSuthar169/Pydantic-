from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Field is data validation
class Patient(BaseModel):


    name : Annotated[str, Field(max_length=50, title = "name of the patient", 
                                               description="less than 50 chars",
                                               examples=['Sandeep', 'Amit'])]
    age : int = Field(gt=0, lt=90)
    email : EmailStr
    linked_url: AnyUrl
    weight : Annotated[float,Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the marrid or not")]
    allergiers: Annotated[Optional[list[str]], Field(default=None, max_length=5)]
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



# 49.86