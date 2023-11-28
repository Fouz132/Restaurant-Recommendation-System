import pandas as pd
import tkinter as tk
from tkinter import ttk
# Define the data structure to store restaurant information
restaurant_data = {
    'restaurants': [
        {
            'name': 'Pizza Place',
            'cuisine': 'Italian',
            'rating': 4.5,
            'proximity': 0.5
        },
        {
            'name': 'Sushi House',
            'cuisine': 'Japanese',
            'rating': 4.2,
            'proximity': 1.2
        },
        {
            'name': 'Taco Bell',
            'cuisine': 'Mexican',
            'rating': 3.8,
            'proximity': 0.8
        },
        {
            'name': 'Curry Palace',
            'cuisine': 'Indian',
            'rating': 4.7,
            'proximity': 1.5
        },
        {
            'name': 'Burger Joint',
            'cuisine': 'American',
            'rating': 4.1,
            'proximity': 0.7
        },
        {
        'name': 'Ramen Spot',
        'cuisine': 'Japanese',
        'rating': 4.0,
        'proximity': 1.0
    },
    {
        'name': 'Pasta House',
        'cuisine': 'Italian',
        'rating': 4.3,
        'proximity': 0.9
    },
    {
        'name': 'Taco Express',
        'cuisine': 'Mexican',
        'rating': 4.1,
        'proximity': 0.6
    },
    {
        'name': 'Spice Haven',
        'cuisine': 'Indian',
        'rating': 4.5,
        'proximity': 1.3
    },
    {
        'name': 'BBQ Grill',
        'cuisine': 'American',
        'rating': 4.2,
        'proximity': 0.5
    },
    {
        'name': 'French Delight',
        'cuisine': 'French',
        'rating': 4.4,
        'proximity': 1.1
    },
    {
        'name': 'Thai Flavor',
        'cuisine': 'Thai',
        'rating': 4.6,
        'proximity': 0.8
    },
    {
        'name': 'Spanish Tapas',
        'cuisine': 'Spanish',
        'rating': 4.2,
        'proximity': 1.4
    },
    {
        'name': 'Chinese Wok',
        'cuisine': 'Chinese',
        'rating': 4.3,
        'proximity': 0.7
    },
    {
        'name': 'Mediterranean Oasis',
        'cuisine': 'Mediterranean',
        'rating': 4.5,
        'proximity': 1.0
    }
    ]
}

# Function to recommend restaurants based on user input
# Function to recommend restaurants based on user input
def recommend_restaurants(cuisine):
    # Convert user input to lowercase to match data
    cuisine = cuisine.lower()

    # Filter restaurants based on cuisine
    filtered_restaurants = []
    for restaurant in restaurant_data['restaurants']:
        if restaurant['cuisine'].lower() == cuisine:
            filtered_restaurants.append(restaurant)

    # Sort restaurants by rating and proximity
    filtered_restaurants.sort(key=lambda restaurant: (restaurant['rating'], restaurant['proximity']), reverse=True)

    # Display recommended restaurants with additional details
    if filtered_restaurants:
        result_text.set(f"Recommended restaurants for {cuisine}:\n")
        for restaurant in filtered_restaurants:
            stars_str = stars(restaurant['rating'])
            result_text.set(result_text.get() + f"{restaurant['name']} - Rating: {restaurant['rating']}, Stars :  {stars_str}, Distance: {restaurant['proximity']} km\n")
    else:
        result_text.set(f"No restaurants found for {cuisine}")

# Rest of the code remains the same


# Function to generate stars based on rating
def stars(rating):
    stars = ""
    for i in range(int(rating)):
        stars += "*"
    return stars

# Modify the on_submit function to take user input and display the result
def on_submit():
    cuisine_input = cuisine_var.get().strip()  # Get user input and remove leading/trailing spaces
    if cuisine_input:
        recommend_restaurants(cuisine_input)
    else:
        result_text.set("Please enter a cuisine type.")

# Create GUI
def on_submit():
    cuisine_input = cuisine_var.get().strip()  # Get user input and remove leading/trailing spaces
    if cuisine_input:
        recommend_restaurants(cuisine_input)
    else:
        result_text.set("Please enter a cuisine type.")

# Create GUI
def on_submit():
    cuisine_input = cuisine_var.get().strip()  # Get user input and remove leading/trailing spaces
    if cuisine_input:
        recommend_restaurants(cuisine_input)
    else:
        result_text.set("Please enter a cuisine type.")

# Create GUI
def on_submit():
    cuisine_input = cuisine_var.get().strip()  # Get user input and remove leading/trailing spaces
    if cuisine_input:
        recommend_restaurants(cuisine_input)
    else:
        result_text.set("Please enter a cuisine type.")

root = tk.Tk()
root.title("Restaurant Recommendation System")

# Set the initial size of the window
root.geometry("500x300")

# GUI components
label = ttk.Label(root, text="Enter the type of cuisine you desire:")
label.pack(pady=10)

cuisine_var = tk.StringVar()
cuisine_entry = ttk.Entry(root, textvariable=cuisine_var)
cuisine_entry.pack(pady=10)

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.pack(pady=10)

root.mainloop()
