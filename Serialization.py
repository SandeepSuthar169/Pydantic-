from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int


class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address


address_dict ={'city': 'UK', 'state': 'gujarat', 'pin': 303085 }

address1 = Address(**address_dict)

patient_dict = {
    'name': 'sandeep',
    'gender': 'male',
    'age': 53,
    'address': address1
}

patient1 = Patient(**patient_dict)

temp  = patient1.model_dump()
teemp = patient1.model_dump(include=['name'])
                          # exclude = ['name', 'gender'] 
                          # exclude = {'address':['state']}    
temp1  = patient1.model_dump_json()

print(temp)
print(type(temp))
print(teemp)
print(' ')
print(temp1)
print(type(temp1))
