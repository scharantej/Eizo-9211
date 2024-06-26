## Design: Website to Learn Japanese with Images Using Flask

### HTML Files

1. **index.html:**
   - Main landing page for the website, displaying a list of categories (e.g., animals, food, nature) related to Japanese vocabulary.
   - Each category will have an associated button that, when clicked, navigates to the category's specific page.

2. **category.html:**
   - Page dedicated to a specific category, displaying a collection of Japanese words with corresponding images.
   - Each word will be represented as a flashcard with its Japanese character, pronunciation, English translation, and image.

### Routes

1. **@app.route('/')**:
   - Handles GET requests for the main landing page (index.html).
   - Queries the database to retrieve a list of categories and passes them to the index.html template.

2. **@app.route('/category/<category_name>')**:
   - Handles GET requests for a specific category page (category.html).
   - Queries the database to retrieve Japanese words and images associated with the provided category name.
   - Passes the retrieved data to the category.html template.