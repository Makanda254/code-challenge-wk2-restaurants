
class Restaurant:
    restaurants =[]
    def __init__(self, name):
        self._name = name
        self.get_reviews= []
        Restaurant.restaurants.append(self)
    
    def get_name(self):
        return self._name
    
    def add_review(self,review):
            self.get_reviews.append(review)

    def reviews(self):
        return self.get_reviews

    def customers(self):
            return list({review.customer for review in self.reviews})

    def average_star_rating(self):  
          if len(self.reviews) == 0:
              return 0
          return sum(review.rating for review in self.reviews) / len(self.reviews)

 
 #Test to return name name of restaurant   
restaurant1 = Restaurant('CJs')
print(restaurant1.get_name()) # output: CJs

restaurant2 = Restaurant("KFC")
print(restaurant2.all_reviews())
        
        