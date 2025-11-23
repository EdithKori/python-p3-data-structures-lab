spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# lib/data_structures.py

def get_names(spicy_foods):
    """Returns a list of the names of all spicy foods."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Returns a list of foods with heat_level > 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Prints each spicy food in the format: Name (Cuisine) | Heat Level: 🌶🌶🌶"""
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the first spicy food whose cuisine matches the given cuisine string."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # if no match found


def print_spiciest_foods(spicy_foods):
    """Prints only the foods with heat_level > 5 using the same format as print_spicy_foods."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    """Returns the average heat level as an integer."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)



def create_spicy_food(spicy_foods, new_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(new_food)
    return spicy_foods
