# Cooking Recipe Recommendation System

A web-based application that helps users discover and search for recipes based on their preferences. The system uses ingredient and cuisine data to recommend delicious recipes with filtering capabilities.

## Features

- 🔍 **Search by Ingredients** - Find recipes by entering ingredients you have
- 🍽️ **Filter by Meal Type** - Browse recipes by meal category (Breakfast, Lunch, Dinner, Snack)
- ⏱️ **Filter by Prep Time** - Find recipes based on cooking time (15, 30, 60 minutes)
- 🖼️ **Recipe Cards** - View recipe details with images and cooking information
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- ⭐ **Quick Recommendations** - Get instant recipe suggestions

## Technologies Used

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

- **Backend/Data Processing:**
  - Python
  - Pandas (data manipulation)
  - Regular Expressions (text cleaning)

- **Data Format:**
  - CSV (Cuisines data)
  - JSON (Recipes data)

## Project Structure

```
Cooking-recipe-recommendation-system/
├── index.html                 # Main landing/search page
├── details.html               # Recipe details page
├── styles.css                 # CSS styling
├── script.js                  # Main JavaScript logic
├── details.js                 # Details page JavaScript
├── cleandataset2.py          # Python data cleaning script
├── recipes.json              # Recipes database
├── cuisines.csv              # Cuisines data
├── image_for_cuisines/       # Recipe images folder
│   └── data/
└── README.md                 # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.x (for data processing)
- A modern web browser

### Installation

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd Cooking-recipe-recommendation-system
   ```

2. **Set up Python environment (if needed):**
   ```bash
   pip install pandas
   ```

3. **Run data cleaning script (optional):**
   ```bash
   python cleandataset2.py
   ```

4. **Open the application:**
   - Open `index.html` in your web browser, or
   - Use a local server:
     ```bash
     # Python 3.x
     python -m http.server 8000
     ```
   - Then navigate to `http://localhost:8000`

## Usage

1. **Landing Page:**
   - Click "Start Cooking" button to begin

2. **Search & Filter:**
   - Enter an ingredient in the search box
   - Select meal type from dropdown
   - Select cooking time preference
   - Click "Submit" to search

3. **View Recipes:**
   - Browse recipe cards displayed
   - Click on a recipe to see full details
   - View ingredients, cooking time, and recipe image

## Data Files

### recipes.json
Contains recipe information including:
- Recipe name
- Ingredients
- Cuisine type
- Meal type
- Prep time
- Image reference

### cuisines.csv
Contains cuisine and ingredient data used for categorization and filtering

### image_for_cuisines/data/
Stores recipe images referenced in the recipes data

## Python Data Cleaning

The `cleandataset2.py` script:
- Loads cuisine data from CSV
- Normalizes and cleans text data
- Matches recipes with their corresponding images
- Removes special characters and standardizes formatting

## Key Functions

### JavaScript (script.js)
- `filterRecipes()` - Filters recipes based on search criteria
- `displayRecipes()` - Renders recipe cards to the page
- `searchByIngredient()` - Searches recipes by ingredient name

### Python (cleandataset2.py)
- `normalize()` - Converts text to lowercase and removes special characters
- `get_words()` - Splits text into individual words
- `find_image()` - Matches recipes to their image files

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

- User authentication and saved favorites
- Nutritional information display
- Recipe ratings and reviews
- Dietary restriction filters
- Recipe difficulty levels
- Video cooking tutorials
- Shopping list generation
- Backend API integration

## Troubleshooting

**Images not loading:**
- Ensure `image_for_cuisines/data/` folder contains recipe images
- Run `cleandataset2.py` to rebuild image mappings

**Recipes not appearing:**
- Verify `recipes.json` is in the root directory
- Check browser console for JavaScript errors (F12)
- Ensure JSON file format is valid

**Search not working:**
- Clear browser cache
- Try different ingredient names
- Check console for any error messages

## Contributing

Feel free to contribute by:
- Adding more recipes
- Improving the UI/UX
- Optimizing search algorithms
- Adding new features

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions:
- Check the troubleshooting section
- Review the browser console for error messages
- Verify all data files are present and properly formatted

---

**Happy Cooking!** 👨‍🍳
