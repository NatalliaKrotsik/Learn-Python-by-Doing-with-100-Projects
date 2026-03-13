from flask import Flask
import json

app = Flask(__name__)

with open('recipes.json') as file:
    recipes = json.load(file)
@app.route('/recipes/<id>')

def get_recipe(id):
    recipe = recipes.get(id)
    if recipe:
        return recipe
    else:
        return "The recipe not found", 404
@app.route('/')
def index2():
    return "Homepage"
app.run(debug=True)


