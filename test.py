# main.py
from customer import Customer
from restaurant import Restaurant
from review import Review


customer1 = Customer("Diana","Marua")
customer2 = Customer("Cici", "Mikal")
restaurant1 = Restaurant("Serena")
restaurant2 = Restaurant("Quiver")


review1 = Review(customer1, restaurant1, 0)
review2 = Review(customer2, restaurant1, 0)
review3 = Review(customer1, restaurant2, 0)
review4 = Review(customer2, restaurant2, 0)

# Prints all instances of Customer class
print("Customers: ", end="\n")
for customer in Customer.customers:
    print(customer.full_name())

# Prints all instances of Restaurant class
print("Restaurants: ", end="\n")
for restaurant in Restaurant.restaurants:
    print(restaurant.get_name())

# Prints average star rating for each restaurant
print("\nAverage Star Ratings: ")
for restaurant in Restaurant.restaurants:
    avg_rating = restaurant.average_star_rating()
    print(f"{restaurant.get_name()}: {avg_rating}")

# Find customers by given name
given_name = "Cici"
print(f"\nCustomers with given name '{given_name}':")
matching_customers = Customer.find_all_by_given_name(given_name)
for customer in matching_customers:
    print(customer.full_name())

# Print number of Reviews for Each customer
print("\nNumber of Reviews for Each customer")
for customer in Customer.all():
    num_reviews = customer.num_reviews()
    print(f"{customer.full_name()}'s Reviews: {num_reviews}")

# Print list of reviews for each customer
print("\nList of Reviews for Each Customer:")
for customer in Customer.all():
    print(f"{customer.full_name()}'s Reviews:")
    for review in customer.reviews:
        print(f"  - Restaurant: {review.restaurant().get_name()}")
        print(f"    Rating: {review.rating()}")