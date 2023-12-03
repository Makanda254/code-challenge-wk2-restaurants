from lib.review import Review
class Customer:
    customers = []
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews=[]
        Customer.customers.append(self)
        
    def get_given_name(self):
        return self._given_name
    
    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            self._given_name = given_name  
        else:
            print("Given name should be a string!")  
            
    given_name = property(get_given_name, set_given_name)
            
    def get_family_name(self):
        return self._family_name
    
    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self._family_name = family_name
        else:
            print("Last name should be a string!")
            
    family_name = property(get_family_name, set_family_name)
    
    def full_name(self):
        return self.given_name + ' ' + self.family_name
    
    def restaurants(self):
        return ({review.restaurant for review in self.reviews})
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)
    
    def num_reviews(self):
        return len(self.reviews)

    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.customers:
            if customer.given_name == name:
                customers.append(customer)
        return customers
    
customer1 = Customer ("Victor", "Makanda")
customer2 = Customer ("Lazaro", "Wachira")
customer3 = Customer ("Vincent", "Mumo")

#Test to get given name
print(customer1.get_given_name())# output: Victor
print(customer2.get_given_name())# output: Lazaro
print(customer3.get_given_name())# output: Vincent

#Test to get family name
print(customer1.get_family_name())# output: Makanda
print(customer2.get_family_name())# output: Wachira
print(customer3.get_family_name())# output: Mumo

#Test to change given name and family name
customer3.set_given_name("Edgar")
customer2.set_family_name("Muraguri")
print(customer3.get_given_name())# output: Edgar
print(customer2.get_family_name())# output: Muraguri

#Test to get full name
print(customer1.full_name())# output: Victor Makanda







    


   


   
    