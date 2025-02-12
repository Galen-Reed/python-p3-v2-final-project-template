# lib/helpers.py
from models.veterinarian import Veterinarian
from models.patient import Patient

def exit_program():
    print("Goodbye!")
    exit()

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

def delete_veterinarian():
    name = input("Enter the veterinarian's name: ")
    if veterinarian := Veterinarian.find_by_name(name):
        veterinarian.delete()
        print(f'Veterinarian {name} deleted')
    else:
        print('Veteriniarian {name} not found')

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patients_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(f'Patient {name} not found')

def find_patient_by_breed():
    breed = input("Enter the patient's breed: ")
    patient = Patient.find_by_breed(breed)
    print(patient) if patient else print(f'Patient {breed} not found')

def create_patient():
    name = input("Enter the patient's name: ")
    breed = input("Enter the patient's breed: ")
    age = input("Enter the patient's age: ")
    try:
        patient = Patient.create(name, breed, int(age))
        print(f'Success: {patient} created')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    name = input("Enter patient's name: ")
    if patient := Patient.find_by_name(name):
        try:
            new_name = input("Enter patient's new name: ")
            breed = input("Enter patient's new breed: ")
            age = input("Enter patient's new age: ")

            patient.update()
            print(f'Success! {patient} has been updated')
        except Exception as exc:
            print(f'Error updating patient: ', exc)
    else:
        print(f'Patient {name} not found')

def delete_patient():
    name = input("Enter patient's name: ")
    if patient := Patient.find_by_name(name):
        patient.delete()
        print(f'Patient {name} has been deleted')
    else:
        print(f'Patient {name} not found')

def list_veterinarian_patients():
    name = input("Enter veterinarian's name: ")
    if veterinarian := Veterinarian.find_by_name(name):
        for patient in veterinarian.patients():
            print(patient)
    else:
        print(f'{veterinarian} not found')
