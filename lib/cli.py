# lib/cli.py
from models.patient import Patient
from models.veterinarian import Veterinarian

from helpers import (
    exit_program,
    list_veterinarians,
    find_veterinarian_by_name,
    find_veterinarian_by_specialty,
    create_veterinarian,
    update_veterinarian,
    delete_veterinarian,
    list_patients,
    find_patients_by_name,
    find_patient_by_breed,
    create_patient,
    update_patient,
    delete_patient,
    list_veterinarian_patients
)

Veterinarian.create_table()

Patient.create_table()


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_veterinarians()
        elif choice == "2":
            find_veterinarian_by_name()
        elif choice == "3":
            find_veterinarian_by_specialty()
        elif choice == "4":
            create_veterinarian()
        elif choice == "5":
            update_veterinarian()
        elif choice == "6":
            delete_veterinarian()
        elif choice == "7":
            list_patients()
        elif choice == "8":
            find_patients_by_name()
        elif choice == "9":
            find_patient_by_breed()
        elif choice == "10":
            create_patient()
        elif choice == "11":
            update_patient()
        elif choice == "12":
            delete_patient()
        elif choice == "13":
            list_veterinarian_patients()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all veterinarians")
    print("2. Find a veterinarian by name")
    print("3. Find a veterinarian by specialty")
    print("4. Add a new veterinarian")
    print("5. Update a veterinarian")
    print("6. Remove a veterinarian")
    print("7. List all patients")
    print("8. Find a patient by name")
    print("9. Find a patient by breed")
    print("10. Add a new patient")
    print("11. Update a patient")
    print("12. Remove a patient")
    print("13. List all patients under a veterinarian")


if __name__ == "__main__":
    main()
