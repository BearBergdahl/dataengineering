people_data = dict()
def people_reader():
        
        customer_list = [] 
        
        try:
            with open("people.data", "r") as file: 
                for line in file:
                    customer_list.append(line) 
                for i in customer_list:
                    customer = i.split(',') 
                    for x in customer:
                         x = x.strip()
                             
                    people_data[customer.pop(0)] = customer
                
        except FileNotFoundError:
            print("File not found, check spelling please")

people_reader()

# _________________________________________________
# Separation between task 1 &2
person_data = people_data
# above is needed in this test to have the data named as in task2.

class Record:
    def __init__(self, person_data):
          self.person_data = person_data
          
         
    def find_and_print(self, security_number):  
        try:
             return self.person_data[security_number]
        except KeyError:
            return(f'Person not found')
       
    def remove(self, security_number):
        if (self.person_data[security_number]):
            del self.person_data[security_number]
            print("Data removed,", len(self.person_data), "records remaining")
        else:
            print("No such data")
            
my_record = Record(person_data)
my_record.remove('850420-0547')