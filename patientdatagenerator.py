import json
import random
import pprint
import names
import sys

# This code is used to generate example patient and module data for the Emeistring program.
# Some shortcuts, like completely random madrs scores, are taken since there is too much data to write and plan manually.

class patient_generator():
    def __init__(self, patient_amount, week_amount, current_week, module_amount):
        self.patient_amount = patient_amount
        self.module_amount = module_amount
        self.week_amount = week_amount
        self.current_week = current_week
        self.patient_names = self._generate_names()
        self.patient_ids = self._generate_patient_ids()
        self.patient_status = self._generate_patient_status()
        self.patient_symptoms = ["Headache", "Concentration_Issues", "Insomnia", "Weakness", "Fatigue", "Gastrointestinal_Problems", "Increased_Heart_Rate", "Sweating", "Hyperventilation"]
        self.treatment_type = ["Depression", "Panic Disorder", "Social Anxiety"]
        self.tasks = ["Reading", "Writing", "Watching_Videos"]
        self.activity_categories = ["Family_or_Friends", "Health", "Free_Time", "Work_or_Study"]
        self.activities = ["Fishing", "Gardening", "Indoor Games", "Job", "Outdoor Games", "Reading", "Shopping", "Sleeping", "Tour", "Exercise", "Writing"]
        self.activity_sentiment = ["Postive", "Negative", "Neutral"]

    def set_patients_amount(self, patient_amount):
        self.patient_amount = patient_amount

    def set_modules_amount(self, module_amount):
        self.module_amount = module_amount

    def _generate_names(self):
        i = 0
        patient_names = []
        while i < self.patient_amount:
            patient_names.append(names.get_full_name())
            i += 1
        return patient_names

    def _generate_patient_ids(self):
        i = 0
        patient_ids = []
        while i < self.patient_amount:
            patient_ids.append(str(random.randrange(1, 10000)))
            i += 1
        return patient_ids

    def _generate_patient_status(self):
        i = 0
        patient_ids = []
        while i < self.patient_amount:
            patient_ids.append(str(random.randrange(1, 10000)))
            i += 1
        return patient_ids

    def generate_data(self, path, data_format):
        if data_format == "json":
            therapist_name = names.get_full_name()
            json_data = {'treatment_program': {'therapist_name': therapist_name,
                                               'therapist_id': str(random.randrange(1,10000)),
                                               'treatment_type': random.choice(self.treatment_type),
                                               'amount_of_modules': self.module_amount,
                                               'amount_of_weeks': self.week_amount,
                                               'current_week': self.current_week},
                         'modules': []}

            i = 1
            while i <= self.module_amount:
                module_data = {}
                module_data["module_id"] = str(i)
                module_data["week"] = str(i)
                module_data["date_started"] = "1-" + str(i+1) + "-2020"
                module_data["completed"] = str(True)
                module_data["date_ended"] = "8" + "-" + str(i + 1) + "-2020"
                module_data["submission_date"] = str(i+3) + "-" + str(i+1) + "-2020"

                if i > self.current_week:
                    module_data["completed"] = str(False)
                    module_data["date_finished"] = "N/A"

                patient_data = []
                j = 1
                while j <= self.patient_amount:
                    patient_active_chance = random.randrange(1, 10)
                    therapist_active_chance = random.randrange(1, 10)

                    madrs_score = random.randrange(0, 60)
                    message_to_therapist = True
                    message_from_therapist = True

                    if i > self.current_week:
                        completion = str(False)
                        message_from_therapist = str(False)
                        message_to_therapist = str(False)
                        madrs_score = "N/A"
                    else:
                        completion = True
                        if patient_active_chance == 1:
                            completion = False
                            message_from_therapist = True
                            message_to_therapist = True
                        if therapist_active_chance == 1:
                            message_from_therapist = False

                    patient_data.append({
                        "patient_id": self.patient_ids[j-1],
                        "patient_name": self.patient_names[j-1],
                        "patient_email": (self.patient_names[j - 1] + "@examplemail.com").replace(" ", "_"),
                        "symptoms": [random.choice(self.patient_symptoms), random.choice(self.patient_symptoms), random.choice(self.patient_symptoms)],
                        "assigned_therapist": therapist_name,
                        "module_completion": completion,
                        "tasks": [random.choice(self.tasks), random.choice(self.tasks)],
                        "activity_category": random.choice(self.activity_categories),
                        "activity": random.choice(self.activities),
                        "activity_sentiment": random.choice(self.activity_sentiment),
                        "message_from_therapist": str(message_from_therapist),
                        "message_to_therapist": str(message_to_therapist),
                        "madrs_score": madrs_score,
                        "last_online": "1-" + str(i+1) + "-2020",
                        "minutes_spent_online": str(random.randrange(100, 500)),
                        })
                    j += 1

                module = {}
                module["module_data"] = module_data
                module["patient_data"] = patient_data

                json_data['modules'].append(module)
                i += 1

            with open(path, 'w') as outfile:
                json.dump(json_data, outfile)


    def print_data(self, path):
        with open(path, 'r') as patient_data:
            pprint.pprint(json.load(patient_data))


def main(args):
    patient_data = patient_generator(module_amount=14, week_amount=14, current_week=10, patient_amount=15)
    patient_data.generate_data("data/patient_data.json", data_format="json")
    patient_data.print_data("data/patient_data.json")

if __name__ == '__main__':
    main(sys.argv)