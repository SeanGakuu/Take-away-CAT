def add_patient(name, age, illness, patient_list):
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    patient_list.append(patient)
    print(f"Patient '{name}' added successfully.\n")

def display_patients(patient_list):
    if not patient_list:
        print("No patients in the list.\n")
    else:
        print("List of Patients:")
        for index, patient in enumerate(patient_list, start=1):
            print(f"{index}. Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
        print()

def search_patient(name, patient_list):
    found = False
    for patient in patient_list:
        if patient['name'].lower() == name.lower():
            print(f"Patient found:")
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            found = True
            break
    if not found:
        print(f"Patient '{name}' not found.\n")

def remove_patient(name, patient_list):
    removed = False
    for patient in patient_list[:]:  # Iterate over a copy of the list to safely remove elements
        if patient['name'].lower() == name.lower():
            patient_list.remove(patient)
            print(f"Patient '{name}' removed successfully.\n")
            removed = True
    if not removed:
        print(f"Patient '{name}' not found.\n")

def main():
    patients = []

    while True:
        print("Hospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter patient's name: ")
            age = input("Enter patient's age: ")
            illness = input("Enter patient's illness: ")
            add_patient(name, age, illness, patients)
        
        elif choice == '2':
            display_patients(patients)
        
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient(name, patients)
        
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient(name, patients)
        
        elif choice == '5':
            print("Exiting program. Thank you!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
