import json
import random
import pprint

modules_amount = 14
patients_amount = 15

tasks_categories = ["Family_or_Friends", "Health", "Free_Time", "Work_or_Study"]
tasks = ["Fishing", "Gardening", "Indoor Games", "Job",
         "Outdoor Games", "Reading", "Shopping", "Sleeping", "Tour", "Exercise", "Writing"]


json_data = {}
json_data['modules'] = []

i = 1
j = 1
while i <= modules_amount:
    patients = []
    j = 1
    while j <= patients_amount:
        patient_active_chance = random.randrange(1, 10)
        therapist_active_chance = random.randrange(1, 10)

        completion = True
        if patient_active_chance == 1:
            completion = False
        therapist_active = True
        if therapist_active_chance == 1:
            therapist_active = False

        patients.append({
            "name": "patient_" + str(j),
            "completion": str(completion),
            "activity_category": random.choice(tasks_categories),
            "activity": random.choice(tasks),
            "therapist_active": str(therapist_active),
            "madris_score": random.randrange(0, 60),
            })
        j += 1

    json_data['modules'].append(
        {
            "module_" + str(i): {"patients": patients},
        }
    )
    i += 1

pprint.pprint(json_data)

with open('data/patient_data.json', 'w') as outfile:
    json.dump(json_data, outfile)