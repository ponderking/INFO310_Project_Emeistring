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
    module_data = {}
    module_data["module_id"] = str(i)
    module_data["date_started"] = "1-" + str(i+1) + "-2020"
    module_data["status"] = str(True)
    module_data["date_finished"] = str(i+3) + "-" + str(i+1) + "-2020"

    if i > 10:
        module_data["status"] = str(False)
        module_data["date_finished"] = "N/A"

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

    json_data['modules'].append([
            {"patients": patients},
            {"module_data": module_data}
    ]
    )
    i += 1

pprint.pprint(json_data['modules'])

with open('data/patient_data.json', 'w') as outfile:
    json.dump(json_data, outfile)