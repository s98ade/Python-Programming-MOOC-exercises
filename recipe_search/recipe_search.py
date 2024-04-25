# Write your solution here
def search_by_name(filename: str, word: str) -> list:
    found_recipes = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            name = lines[i].strip().lower()
            time = int(lines[i+1].strip())
            ingredients = []
            i += 2
            while i < len(lines) and lines[i].strip() != "":
                ingredients.append(lines[i].strip().lower())
                i += 1
            
            if word.lower() in name:
                found_recipes.append(name.title())  
            i += 1
    
    return found_recipes

def search_by_time(filename: str, prep_time: int) -> list:
    found_recipes = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            name = lines[i].strip().lower()
            time = int(lines[i+1].strip())
            ingredients = []
            i += 2
            while i < len(lines) and lines[i].strip() != "":
                ingredients.append(lines[i].strip().lower())
                i += 1
            
            if time <= prep_time:
                found_recipes.append(f"{name.title()}, preperation time {time} min")  
            i += 1
    
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    found_recipes = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            name = lines[i].strip()
            time = int(lines[i+1].strip())
            ingredients = []
            i += 2
            while i < len(lines) and lines[i].strip() != "":
                ingredients.append(lines[i].strip())
                i += 1
            
            if any(ingredient.lower() in ing.lower() for ing in ingredients):
                found_recipes.append(f"{name}, preparation time {time} min")
            
            # Skip the empty line after the recipe
            i += 1
    
    return found_recipes

if __name__ == "__main__":
    #found_recipes = search_by_name("recipes1.txt", "cake")
    #for recipe in found_recipes:
        #print(recipe)
    
    #found_recipes = search_by_time("recipes1.txt", 20)
    #for recipe in found_recipes:
        #print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)