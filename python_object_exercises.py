# Python Object Exercises

class Person:
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person in self.num_unique_people_greeted:
            pass
        else:
            self.num_unique_people_greeted.append(other_person)


    def print_contact_info(self):
        print("Sonny's email: {}, Sonny's phone number: {}".format(self.email, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)
        print("{} is now friends with {}!".format(self.name, other_person.name))

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def num_unique(self):
        return(len(self.num_unique_people_greeted))



Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
Jake = Person("Jake", "jake@aol.com", "4040404040")

Sonny.greet(Jordan)
Jordan.greet(Sonny)
Sonny.greet(Jake)
Jordan.greet(Sonny)

# print("{}\'s email is {} and his phone number is {}!".format(Sonny.name, Sonny.email, Sonny.phone))
# print("{}\'s email is {} and his phone number is {}!".format(Jordan.name, Jordan.email, Jordan.phone))

# Sonny.print_contact_info()

# These are no longer necessary
#Jordan.friends.append(Sonny)
#print(len(Jordan.friends))  
#print("{}".format(list(Jordan.friends)))

#Sonny.add_friend(Jordan)
#Sonny.num_friends()
#print(Sonny.greeting_count)
#print(Jordan)

print(Sonny.num_unique())


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))

car = Vehicle('Nissan', 'Leaf', '2015')

car.print_info()

