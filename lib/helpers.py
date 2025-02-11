# lib/helpers.py
from models.veterinarian import Veterinarian
from models.patient import Patient


def helper_1():
    print("Performing useful function#1.")

def list_veterinarians():
    veterinarians = Veterinarian.get_all()
    for veterinarian in veterinarians:
        print(veterinarian)

def find_veterinarian_by_name():
    name = input("Enter the veterinarians's name: ")
    veterinarian = Veterinarian.find_by_name(name)
    print(veterinarian) if veterinarian else print(
        f'Veterinarian {name} not found')
    
def find_veterinarian_by_specialty():
    specialty = input("Enter the desired specialty: ")
    veterinarian = Veterinarian.find_by_id(specialty)
    print(veterinarian) if veterinarian else print(f' {specialty} veterinarian not found')

def create_veterinarian():
    name = input("Enter the veterinarian's name: ")
    specialty = input("Enter the veterinarian's specialty: ")
    try: 
        veterinarian = Veterinarian.create(name, specialty)
        print(f'Success: {veterinarian}')
    except Exception as exc:
        print(f'Error creating veterinarian: ', exc)

def update_veterinarian():
    name = input("Enter the veterinarian's name: ")
    if veterinarian := Veterinarian.find_by_name(name):
        try:
            name = input("Enter the veterinarian's new name: ")
            veterinarian.name = name
            specialty = input("Enter the veterinarian's new specialty: ")
            veterinarian.specialty = specialty

            veterinarian.update()
            print(f'Succes: {veterinarian}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Veterinarian {name} not found')