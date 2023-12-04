from review import Review
from customer import Customer
class Restaurant:
    restaurants =[]
    def __init__(self, name):
        self._name = name
        self.get_reviews= []
        Restaurant.restaurants.append(self)
    
    def get_name(self):
        return self._name
    
    def add_review(self, review):
            self.get_reviews.append(review)

    def reviews(self):
        return self.get_reviews

    def customers(self):
            return list({review.customer for review in self.get_reviews})
   

    def average_star_rating(self):  
          if not self.get_reviews:
              return 0
          return sum(review.rating() for review in self.get_reviews) / len(self.get_reviews)
      
    @classmethod   
    def all(cls):
        return cls.restaurants

 
 #Test to return name name of restaurant   
restaurant1 = Restaurant('CJs')
print(restaurant1.get_name()) # output: CJs

restaurant2 = Restaurant("KFC")
print(restaurant2.reviews())
      
customer4 = Customer("Victor", "Makanda")

review1 = Review(customer4, restaurant1, 5.5)
  





        