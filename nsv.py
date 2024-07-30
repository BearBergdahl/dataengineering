class Record:
    def __init__(self, people_data) -> None:
        self.people_data = people_data
       


    def find_and_print(self, searchstring) -> None:
            
        try:
            cst = self.people_data[searchstring]
        except KeyError:
            print('Person not found.')
            
        if isinstance (cst, list):
            print(f'{cst[0]}')
            print(f'{cst[1]}')
            print(f'{cst[2]}')
            print(f'{cst[3]}')
            print(f'{cst[4]}'.strip())
    

    def remove(self, searchstring) -> None:
        del self.people_data[searchstring] 
        amount = len(people_data[searchstring])

        if people_data[searchstring] < 0:
           print(f'Data removed, {amount} records remaining')




with open('people.data') as people:
    peoplelist = people.readlines()

people_data = dict()

for person in peoplelist:
    aperson = person.split(';')
    key = aperson.pop(0)
    aperson[3] = aperson[3].strip()
    value = aperson
    people_data[key] = value

	
my_record = Record(people_data)
my_record.remove('780811-1565')