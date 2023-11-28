Restaurant Recommendation System
Overview
This program is a simple restaurant recommendation system with a graphical user interface (GUI) built using Tkinter. It allows users to input a cuisine type, and the system recommends restaurants based on the entered cuisine. The recommendations are sorted by restaurant rating and proximity.

Instructions
Dependencies:

Ensure you have Python installed on your system.
The program uses the pandas library for data handling and tkinter for GUI. You can install them using:
bash
Copy code
pip install pandas
Run the Program:

Execute the main program file restaurant_recommendation_system.py to launch the GUI.
bash
Copy code
python restaurant_recommendation_system.py
GUI Usage:

Enter the desired cuisine type in the provided entry field.
Click the "Submit" button to get restaurant recommendations.
The recommendations will be displayed below the entry field.
Unit Tests:

The program includes unit tests to ensure the functionality of the recommendation algorithm.
Run the unit tests using the following command:
bash
Copy code
python test_recommendations.py
Additional Information
Data Structure:

Restaurant information is stored in a dictionary with the key 'restaurants'.
Each restaurant is represented by a dictionary with keys 'name', 'cuisine', 'rating', and 'proximity'.
Recommendation Algorithm:

The program filters restaurants based on user-input cuisine, sorts them by rating and proximity, and displays the recommendations.
Unit Tests:

The test_recommendations.py file contains unit tests for the recommendation function.
The setUp and tearDown methods handle GUI initialization and cleanup for testing.
Screenshots:

Screenshots of the GUI are available in the Git repository for reference.
Git Repository
The Git repository for this project includes:
restaurant_recommendation_system.py: Main program file.
test_recommendations.py: Unit tests.
Screenshots folder: GUI screenshots.
README.md: This documentation file.