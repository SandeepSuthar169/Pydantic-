from pydantic import (BaseModel, 
                      EmailStr, 
                      AnyUrl, 
                      Field, 
                      field_validator, 
                      model_validator)
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
#---------------- 
    @model_validator(mode ='after')
    def validate_emergenct_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError('patients older than 60 must have an energency contact')
        
        return model
    

#--------------- email
    @field_validator('email')
    @classmethod
    
    def email_validaor(cls, value):
        valid_domains  = ['hdfc.com', 'icici.com']
        domail_name = value.split("@")[-1]    # @gmailcom

        if domail_name not in  valid_domains:
            raise ValueError('Not a valud domain')
        
        return value
        
#--------------- name
    @field_validator('name', mode="before")    # model = after,  before
    @classmethod
    def transform_name(cls, value):
        return value.upper()

#--------------- age
    @field_validator('age', mode ='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            return ValueError('Age should be in between 0 and 100')
        

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)

patient_info = {'name':'sandeep', 
                'email':'abc@icici.com', 
                'age': 90, 
                'weight': 75.2, 
                'married': True, 
                'allergies': ['pollen', 'dust'], 
                'contact_details':{'phone':'2353462', 
                                   'emergency': '2525252525'}
                }

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
