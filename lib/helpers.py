# lib/helpers.py
from models.veterinarian import Veterinarian
from models.patient import Patient

def exit_program():
    print("Goodbye!")
    exit()

def list_veterinarians():
    veterinarians = Veterinarian.get_all()
    for veterinarian in veterinarians:
        print(f"\n{veterinarian}\n")

def find_veterinarian_by_name():
    name = input("Enter the veterinarians's name: ")
    veterinarian = Veterinarian.find_by_name(name)
    print(f"\n{veterinarian}\n") if veterinarian else print(
        f'\nVeterinarian {name} not found\n')
    
def find_veterinarian_by_specialty():
    specialty = input("Enter the desired specialty: ")
    veterinarian = Veterinarian.find_by_specialty(specialty)
    print(f"\n{veterinarian}\n") if veterinarian else print(f'\n {specialty} veterinarian not found\n')

def create_veterinarian():
    name = input("Enter the veterinarian's name: ")
    specialty = input("Enter the veterinarian's specialty: ")
    try: 
        veterinarian = Veterinarian.create(name, specialty)
        print(f'\nSuccess! {veterinarian}\n')
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
            print(f'\nSuccess! {veterinarian}\n')
        except Exception as exc:
            print("Error updating veterinarian: ", exc)
    else:
        print(f'\nVeterinarian {name} not found\n')

def delete_veterinarian():
    name = input("Enter the veterinarian's name: ")
    if veterinarian := Veterinarian.find_by_name(name):
        veterinarian.delete()
        print(f'\nVeterinarian {name} deleted\n')
    else:
        print('\nVeteriniarian {name} not found\n')

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patients_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(f"\n{patient}\n") if patient else print(f'\nPatient {name} not found\n')

def find_patient_by_breed():
    breed = input("Enter the patient's breed: ")
    patient = Patient.find_by_breed(breed)
    print(f"\n{patient}\n") if patient else print(f'\nPatient {breed} not found\n')

def create_patient():
    name = input("Enter the patient's name: ")
    breed = input("Enter the patient's breed: ")
    age = input("Enter the patient's age: ")
    veterinarian_name = input("Enter the patient's veterinarian name: ")
    try:
        patient = Patient.create(name, breed, int(age), veterinarian_name)
        print(f'\nSuccess! {patient} created\n')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    name = input("Enter patient's name: ")
    if patient := Patient.find_by_name(name):
        try:
            new_name = input("Enter patient's new name: ")
            new_breed = input("Enter patient's new breed: ")
            new_age = input("Enter patient's new age: ")
            new_veterinarian_name = input("Enter patient's new veterinarian name: ")

            veterinarian_id = Veterinarian.get_id_by_name(new_veterinarian_name)

            if veterinarian_id is None:
                print(f'Veterinarian {new_veterinarian_name} not found. Please add them first')

            patient.name = new_name
            patient.breed = new_breed
            patient.age = int(new_age)
            patient.veterinarian_id = veterinarian_id

            patient.update()
            print(f'\nSuccess! {patient} has been updated\n')
        except Exception as exc:
            print(f'Error updating patient: ', exc)
    else:
        print(f'\nPatient {name} not found\n')

def delete_patient():
    name = input("Enter patient's name: ")
    if patient := Patient.find_by_name(name):
        patient.delete()
        print(f'\nPatient {name} has been deleted\n')
    else:
        print(f'\nPatient {name} not found\n')

def list_veterinarian_patients():
    name = input("Enter veterinarian's name: ")
    if veterinarian := Veterinarian.find_by_name(name):
        for patient in veterinarian.patients():
            print(f"\n{patient}\n")
    else:
        print(f'\n{veterinarian} not found\n')
