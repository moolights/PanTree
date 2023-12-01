class CookingDatabase:
    def __init__(self):
        self.ingredients = [
            'flour', 'sugar', 'eggs', 'butter', 'salt', 'cheese', 'pepper', 'olive oil', 'garlic', 'onion', 'tomato',
            'milk', 'cream', 'cheese', 'bacon', 'chicken', 'beef', 'pork', 'shrimp', 'rice', 'pasta',
            'potato', 'carrot', 'bell pepper', 'broccoli', 'spinach', 'lettuce', 'cucumber', 'zucchini',
            'lemon', 'lime', 'orange', 'apple', 'banana', 'strawberry', 'blueberry', 'raspberry', 'avocado',
            'cilantro', 'parsley', 'basil', 'thyme', 'rosemary', 'oregano', 'cumin', 'coriander', 'paprika',
            'cinnamon', 'nutmeg', 'vanilla extract', 'honey', 'soy sauce', 'vinegar', 'mustard', 'ketchup',
            'mayonnaise', 'hot sauce', 'worcestershire sauce', 'maple syrup', 'chocolate', 'nutella', 'almond',
            'peanut butter', 'quinoa', 'black beans', 'chickpeas', 'lentils', 'coconut milk', 'bread crumbs',
            'baking powder', 'baking soda', 'yeast', 'cocoa powder', 'powdered sugar', 'brown sugar', 'white sugar',
            'vanilla sugar', 'cornstarch', 'cornmeal', 'nutritional yeast', 'molasses', 'coconut oil', 'sesame oil',
            'sunflower oil', 'vegetable broth', 'chicken broth', 'beef broth', 'wine', 'beer', 'whiskey', 'rum',
            'quail eggs', 'duck eggs', 'turmeric', 'bay leaves', 'cardamom', 'cloves', 'allspice', 'turkey',
            'cranberries', 'pumpkin', 'sweet potato', 'kiwi', 'pomegranate', 'ginger', 'shallot', 'mushroom',
            'walnut', 'pine nuts', 'cashew', 'pecan', 'sun-dried tomatoes', 'anchovies', 'feta cheese', 'goat cheese',
            'blue cheese', 'mozzarella', 'parmesan', 'gorgonzola', 'ricotta', 'cheddar', 'hummus', 'sour cream',
            'greek yogurt', 'salsa', 'guacamole', 'tahini'
            # Add more ingredients as needed
        ]

def main():
    cooking_db = CookingDatabase()

    while True:
        print("\n1. Display Ingredients")
        print("2. Get Ingredient Details")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            cooking_db.display_ingredients()
        elif choice == '2':
            ingredient_name = input("Enter the ingredient name: ").lower()
            details = cooking_db.get_ingredient_details(ingredient_name)
            if details:
                print(f"Details for {ingredient_name.capitalize()}:")
                print(f"Category: {details['category']}")
                print(f"Quantity Unit: {details['quantity_unit']}")
            else:
                print(f"{ingredient_name.capitalize()} not found in the database.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
