# code-challenge-wk2-restaurants

# Table of Contents
* Introduction
* Deliverables
* Installation
* Known Bugs
* Technologies used
* License
* Support


# Introduction
This is a Python application designed to manage restaurant reviews from customers. It allows you to create and manage customers, restaurants, and reviews associated with them.

# Deliverables
# Initializers, Readers, and Writers
#  Customer
- `Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - should be able to change after the customer is created
- `Customer family_name()`
  - returns the customer's family name
  - should be able to change after the customer is created
- `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - returns **all** of the customer instances
# Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created
 
# Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews
# Object Relationship Methods
#  Review
- `Review customer()`
  - returns the customer object for that review
  - Once a review is created, should not be able to change the customer
- `Review restaurant()`
  - returns the restaurant object for that given review
  - Once a review is created, should not be able to change the restaurant
# Restaurant
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
# Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
 
# Aggregate and Association Methods
# Customer
- `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored
- `Customer find_by_name(name)` class method
  - given a string of a **full name**, returns the **first customer** whose full name matches
- `Customer find_all_by_given_name(name)` class method
  - given a string of a given name, returns an **list** containing all customers with that given name
 
# Restaurant
- `Restaurant average_star_rating()`
  - returns the average star rating for a restaurant based on its reviews
  - Reminder: you can calculate the average by adding up all the ratings and dividing by the number of ratings.

## Known Bugs
The application works well.

## Technologies used
- Terminal
- Python

# License
This project is licensed under the MIT License.

## Support and contact details
- email :: victormakanda254@gmail.com
- phone :: +254768918629
