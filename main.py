
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Sample data objects (replace these with actual data from database in a real application)
categories = ["Animals", "Food", "Nature"]

animal_words = [
    {"japanese": "ねこ", "pronunciation": "neko", "english": "cat", "image": "cat.jpg"},
    {"japanese": "いぬ", "pronunciation": "inu", "english": "dog", "image": "dog.jpg"},
    {"japanese": "うさぎ", "pronunciation": "usagi", "english": "rabbit", "image": "rabbit.jpg"},
]

food_words = [
    {"japanese": "すし", "pronunciation": "sushi", "english": "sushi", "image": "sushi.jpg"},
    {"japanese": "ラーメン", "pronunciation": "ramen", "english": "ramen", "image": "ramen.jpg"},
    {"japanese": "おにぎり", "pronunciation": "onigiri", "english": "rice ball", "image": "onigiri.jpg"},
]

nature_words = [
    {"japanese": "山", "pronunciation": "yama", "english": "mountain", "image": "mountain.jpg"},
    {"japanese": "海", "pronunciation": "umi", "english": "sea", "image": "sea.jpg"},
    {"japanese": "空", "pronunciation": "sora", "english": "sky", "image": "sky.jpg"},
]

# Define the main route
@app.route('/')
def index():
    # Render the index.html template with the list of categories
    return render_template('index.html', categories=categories)

# Define the category route
@app.route('/category/<category_name>')
def category(category_name):
    # Get the list of words and images for the specified category
    if category_name == "Animals":
        words = animal_words
    elif category_name == "Food":
        words = food_words
    elif category_name == "Nature":
        words = nature_words
    
    # Render the category.html template with the list of words and images
    return render_template('category.html', category_name=category_name, words=words)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
