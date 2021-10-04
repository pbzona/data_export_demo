import random
from faker import Faker
from faker.providers import internet, geo, person, job, company

fake = Faker()
fake.add_provider(internet)
fake.add_provider(geo)
fake.add_provider(person)
fake.add_provider(job)
fake.add_provider(company)

class User:
    def __init__(self):
        self.name = fake.name()
        self.email = fake.free_email()
        self.ip = fake.ipv4()
        self.state = fake.state_abbr()
        self.zip = fake.zipcode_in_state(self.state)
        self.job = fake.job()
        self.company = fake.company()
        self.income = random.randint(0, 350) * 500
        self.beta = False

        self.context = {}
        
        self.create_context()
    
    def create_context(self):
        beta_probability = 15 # Percentage chance the user ends up in part of the beta group
        if random.randint(0, 100) < beta_probability:
            self.beta = True

        self.context = {
            "key" : self.email,
            "country" : "USA",
            "name": self.name,
            "ip": self.ip,
            "email": self.email,
            "name": self.name,
            "custom" : {
                "state" : self.state,
                "zip_code": self.zip,
                "job": self.job,
                "company": self.company,
                "income": self.income,
                "beta": self.beta
            }
        }

    def get_context(self):
        return self.context

    def debug(self):
        print("==========")
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("IP Address: ", self.ip)
        print("State: ", self.state)
        print("ZIP Code: ", self.zip)
        print("Job:", self.job)
        print("Company: ", self.company)
        print("Income: $", self.income)
        print("Beta: ", self.beta)
        print("==========")