from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict ={ 'city': 'UK', 'state': 'gujarat', 'pin': 303085 }

address1 = Address(**address_dict)

patient_dict = {
    'name': 'sandeep',
    'gender': 'male',
    'age': 53,
    'address': address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)


