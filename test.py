# main.py
from customer import Customer
from restaurant import Restaurant
from review import Review

# SAMPLE DATA
customer1 = Customer("John", "Mark")
customer2 = Customer("Martin", "Tyler")
restaurant1 = Restaurant("Italian restaurant")
restaurant2 = Restaurant("Chicken Inn")

# REVIEWS SAMPLE DATA
review1 = Review(customer1, restaurant1, 6.5)
review2 = Review(customer2, restaurant1, 7.5)
review3 = Review(customer1, restaurant2, 9)
review4 = Review(customer2, restaurant2, 4.5)

# Print all customers
print("All Customers: ")
for customer in Customer.all():
    print(customer.full_name)

# Print all restaurants
print("\nAll Restaurants: ")
for restaurant in Restaurant.all():
    print(restaurant.get_name)

# Print average star rating for each restaurant
print("\nAverage Star Ratings: ")
for restaurant in Restaurant.all():
    avg_rating = restaurant.average_star_rating()
    print(f"{restaurant.get_name}: {avg_rating}")

# Find customers by given name
given_name = "Martin"
print(f"\nCustomers with given name '{given_name}':")
matching_customers = Customer.find_all_by_given_name(given_name)
for customer in matching_customers:
    print(customer.full_name)

# Print number of Reviews for Each customer
print("\nNumber of Reviews for Each customer")
for customer in Customer.all():
    num_reviews = customer.num_reviews
    print(f"{customer.full_name}'s Reviews: {num_reviews}")

# Print list of reviews for each customer
print("\nList of Reviews for Each Customer:")
for customer in Customer.all():
    print(f"{customer.full_name}'s Reviews:")
    for review in customer.reviews:
        print(f"  - Restaurant: {review.restaurant().get_name}")
        print(f"    Rating: {review.get_rating()}")