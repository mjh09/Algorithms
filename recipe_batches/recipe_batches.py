#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  # check if recipe ingredients are avaialable
  ing_set = set(ingredients.keys())
  rec_set = set(recipe.keys())
  if rec_set.issubset(ing_set) == False: 
    return 0

  batches_dict = {key: ingredients[key]//recipe[key] for key in recipe.keys() & ingredients.keys()}

  return min(batches_dict.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))