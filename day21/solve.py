import re

def parseInput(recipes):
    foods = []

    for recipe in recipes:
        extracted = re.match(r'(.+?) \(contains (.+?)\)', recipe)
        ingredients = extracted.group(1).split(' ')
        allergens = extracted.group(2).split(', ')
        
        foods.append((ingredients, allergens))
    
    return foods

def part1(recipes):
    occurrences = {}
    allergenToIng = {}

    for ingredients, allergens in recipes:
        for ingredient in ingredients:
            if ingredient not in occurrences.keys():
                occurrences[ingredient] = 1
            else:
                occurrences[ingredient] += 1
        
        for allergen in allergens:
            if allergen not in allergenToIng.keys():
                allergenToIng[allergen] = set(ingredients)
            else:
                allergenToIng[allergen] = set(ingredients).intersection(allergenToIng[allergen])

    allAllergic = set()

    for ingredients in allergenToIng.values():
        allAllergic.update(ingredients)

    nonAllergic = sum([occurrences[ingredient] for ingredient in set(occurrences.keys()).difference(allAllergic)])

    print(nonAllergic)

def part2(recipes):
    allergenToIng = {}

    for ingredients, allergens in recipes:
        for allergen in allergens:
            if allergen not in allergenToIng.keys():
                allergenToIng[allergen] = set(ingredients)
            else:
                allergenToIng[allergen] = set(ingredients).intersection(allergenToIng[allergen])
            
    confirmed = set()
    allergenWithIng = []

    while len(allergenToIng.keys()) > len(allergenWithIng):
        for allergen, ingredients in allergenToIng.items():
            unconfirmed = set(ingredients).difference(confirmed)

            if len(unconfirmed) == 1:
                newFind = unconfirmed.pop()
                allergenWithIng.append((allergen, newFind))
                confirmed.add(newFind)
    
    print(",".join(pair[1] for pair in sorted(allergenWithIng)))

recipes = [line.strip() for line in open('day21/input.txt', 'r')]
parsed = parseInput(recipes)
part1(parsed)
part2(parsed)