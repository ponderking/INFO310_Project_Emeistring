import json
import random
import pprint
import names
import sys

# This code is used to generate example patient and module data for the Emeistring program.

class patient_generator():
    def __init__(self, patient_amount, module_amount):
        self.patient_amount = patient_amount
        self.module_amount = module_amount
        self.patient_names = self._generate_names()
        self.task_categories = ["Family_or_Friends", "Health", "Free_Time", "Work_or_Study"]
        self.tasks = ["Fishing", "Gardening", "Indoor Games", "Job",
                     "Outdoor Games", "Reading", "Shopping", "Sleeping", "Tour", "Exercise", "Writing"]

    def set_patients_amount(self, patient_amount):
        self.patient_amount = patient_amount

    def set_modules_amount(self, module_amount):
        self.modul_amount = module_amount

    def _generate_names(self):
        i = 0
        patient_names = []
        while i < self.patient_amount:
            patient_names.append(names.get_full_name())
            i += 1
        return patient_names

    def generate_data(self, path, format):

        if format == "json":
            json_data = {}
            json_data['modules'] = []

            i = 1
            while i <= self.module_amount:
                module_data = {}
                module_data["module_id"] = str(i)
                module_data["date_started"] = "1-" + str(i+1) + "-2020"
                module_data["status"] = str(True)
                module_data["date_finished"] = str(i+3) + "-" + str(i+1) + "-2020"

                if i > 10:
                    module_data["status"] = str(False)
                    module_data["date_finished"] = "N/A"

                patient_data = []
                j = 1
                while j <= self.patient_amount:
                    patient_active_chance = random.randrange(1, 10)
                    therapist_active_chance = random.randrange(1, 10)

                    completion = True
                    if patient_active_chance == 1:
                        completion = False
                    therapist_active = True
                    if therapist_active_chance == 1:
                        therapist_active = False

                    patient_data.append({
                        "name": self.patient_names[j-1],
                        "completion": str(completion),
                        "activity_category": random.choice(self.task_categories),
                        "activity": random.choice(self.tasks),
                        "therapist_active": str(therapist_active),
                        "madris_score": random.randrange(0, 60),
                        })
                    j += 1

                module = {}
                module["module_data"] = module_data
                module["patient_data"] = patient_data

                json_data['modules'].append(module)
                i += 1

            with open('data/patient_data.json', 'w') as outfile:
                json.dump(json_data, outfile)


    def print_data(self, path):
        with open(path, 'r') as patient_data:
            pprint.pprint(json.load(patient_data))


def main(args):
    patient_data = patient_generator(module_amount=14, patient_amount=15)
    patient_data.generate_data("data/patient_data.json", format="json")
    patient_data.print_data("data/patient_data.json")

if __name__ == '__main__':
    main(sys.argv)