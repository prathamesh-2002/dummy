knowledge_base = {
    "cold": ["headache", "runny nose", "sneezing", "sore throat", "fever"],
    "influenza": ["fever", "chills", "body ache", "sore throat", "runny nose"],
    "typhoid": ["fever", "abdominal pain", "poor appetite", "headache"],
    "chicken pox": ["rash", "body ache", "fever"],
    "measles": ["rash", "fever", "conjunctivitis"],
    "malaria": ["fever", "sweating", "headache", "nausea"]
}

print("Medical Diagnosis Expert System")

while True:
    search_option = input("Enter '1' to search for diseases by symptoms or '2' to search for symptoms by disease: ")

    if search_option == "1":
        symptoms_input = input("Enter the symptoms (comma-separated values): ")
        symptoms = [s.strip() for s in symptoms_input.split(",")]

        matching_diseases = []
        for disease,disease_symptoms in knowledge_base.items():
            if set(symptoms).intersection(set(disease_symptoms)):
                matching_diseases.append(disease)

        if matching_diseases:
            print("Matching diseases:")
            for disease in matching_diseases:
                print(disease)
        else:
            print("No matching diseases found.")

    elif search_option == "2":
        disease = input("Enter the name of the disease: ")

        if disease in knowledge_base:
            print(f"Symptoms of {disease}:")
            for symptom in knowledge_base[disease]:
                print(symptom)
        else:
            print("Disease not found in the knowledge base.")

    else:
        print("Invalid input. Please try again.")

    continue_search = input("Do you want to continue? (yes/no): ")
    if continue_search.lower() != "yes":
        break

print("Thank you for using the Expert system!")