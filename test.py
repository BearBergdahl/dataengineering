class Record():
    def __init__(self, database):
        self.database = database
        
    def find_and_print(self, ssn):
        try:
            recordentry = self.database[ssn]
            print(ssn)
            for each in recordentry:
                print(each)
        except KeyError:
            print('Person not found')

    def remove(self,ssn):
        try:
            del self.database[ssn]
            print(f'Data removed, {len(self.database)} records remaining')
        except KeyError:
            print('No such data')

peoplelist = []
with open('people.data') as people:
    peoplelist = people.readlines()

people_data = dict()

for person in peoplelist:
    aperson = person.split(';')
    key = aperson.pop(0)
    aperson[3] = aperson[3].strip()
    value = aperson
    people_data[key] = value



a_record = Record(people_data)

a_record.find_and_print('707908-6445')
a_record.remove('707908-6445')

a_record.find_and_print('700908-6445')
a_record.remove('700908-6445')