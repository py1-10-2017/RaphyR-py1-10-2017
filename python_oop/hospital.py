class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = 0

class Hospital(Patient):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, patient):
        patient.bed_number += 1
        self.patients.append(patient)
        if self.capacity > len(self.patients):
            print "Great! There's enough space"
        else:
            print "Sorry not enough space"
        return self
    def discharge(self, patient):
        patient.bed_number = 'none'
        self.patients.remove(patient)
        print "Just removed: " + patient.name + " " + "Bed number " + patient.bed_number
        return self


first_patient = Patient(1, 'Harry Hunter', 'alchohol')
second_patient = Patient(2, 'Jessica Hunter', 'milk')
third_patient = Patient(3, 'Margarita Hunter', 'everything')
hospital1 = Hospital('Palmetto', 5)
hospital1.admit(first_patient).admit(second_patient).admit(third_patient)
hospital1.discharge(second_patient)
