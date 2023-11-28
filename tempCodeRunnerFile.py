import unittest
from unittest.mock import patch
from tkinter import StringVar, Tk
from Restaurant_Recommendation_system import recommend_restaurants

class TestRecommendations(unittest.TestCase):
    restaurant_data = {
        'restaurants': [
            {
                'name': 'Pizza Place',
                'cuisine': 'Italian',
                'rating': 4.5,
                'proximity': 0.5
            },
            # ... (other restaurant entries)
        ]
    }

    def setUp(self):
        self.root = Tk()
        self.root.geometry("500x300")  # Set the initial size of the window

    def tearDown(self):
        self.root.destroy()

    def test_recommend_restaurants_valid_cuisine(self):
        with patch('tkinter.simpledialog.askstring', return_value='italian'):
            result_text = StringVar()

            with patch('Restaurant_Recommendation_system.result_text', result_text):
                recommend_restaurants("italian")

            output = result_text.get().strip()

            self.assertIn("Recommended restaurants for italian:", output)
            self.assertIn("Pizza Place", output)
            self.assertIn("4.5", output)
            self.assertIn("0.5 km", output)

    def test_recommend_restaurants_invalid_cuisine(self):
        with patch('tkinter.simpledialog.askstring', return_value='vegetarian'):
            result_text = StringVar()
            
            with patch('Restaurant_Recommendation_system.result_text', result_text):
                recommend_restaurants("vegetarian")

            output = result_text.get().strip()

            self.assertIn("No restaurants found for vegetarian", output)

    def test_recommend_restaurants_empty_input(self):
        with patch('tkinter.simpledialog.askstring', return_value=''):
            result_text = StringVar()

            with patch('Restaurant_Recommendation_system.result_text', result_text):
                recommend_restaurants("")

            output = result_text.get().strip()

            self.assertIn("No restaurants found for", output)

if __name__ == '__main__':
    unittest.main()
