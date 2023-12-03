from customer import Customer
from restaurant import Restaurant
class Review:
    reviews=[]
    def __init__(self, customer, restaurant, rating):
        self.get_rating = rating
        self._customer = customer
        self._restaurant = restaurant
        Review.reviews.append(self)
    
    def rating(self):
        return self.get_rating
     
    def cutsomer_obj(self):
        return self._customer
  
    def restaurant_obj(self):
        return self._restaurant
    
    @classmethod
    def get_reviews(cls):
        return cls.reviews
    


review1= Review("customer1", "restaurant1", 7.5)
print(review1.restaurant_obj()) # output: restaurant1

review2= Review("customer2", "restaurant2", 3.5)
print(review2.cutsomer_obj()) # output: customer2


    
    
        
        
    