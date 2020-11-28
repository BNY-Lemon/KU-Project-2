from flask import Flask, render_template, jsonify, redirect
import pymongo
from bson.json_util import dumps

# Create an instance of our Flask app.
app = Flask(__name__)

# Pass connection to the pymongo instance.
client = pymongo.MongoClient("mongodb://DVGroup3:sealab2021@cluster0-shard-00-00.g3kws.mongodb.net:27017,cluster0-shard-00-01.g3kws.mongodb.net:27017,cluster0-shard-00-02.g3kws.mongodb.net:27017/happiness?ssl=true&replicaSet=atlas-183d98-shard-0&authSource=admin&retryWrites=true&w=majority")

# Connect to a database. Will create one if not already available.
db = client.happiness

# Set route
@app.route('/')
def index():
    # Return the template with the happiness list passed in
    return render_template('index.html')

# page routes    
@app.route('/heatMap.html')
def heat_map():
    # Return the template with the happiness list passed in
    return render_template('heatMap.html')

@app.route('/visualization.html')
def plot():
    # Return the template with the happiness list passed in
    return render_template('visualization.html')


# create api route for each table
@app.route("/api/v1.0/master")
def master():
    master_table = db.master.find()
    # convert to list
    master_table = list(master_table)
    print(master_table)
    
    return dumps(master_table)

@app.route("/api/v1.0/happiness")
def happiness():
    happiness_table = db.happiness.find()
    # convert to list
    happiness_table = list(happiness_table)
    print(happiness_table)
    
    return dumps(happiness_table)


@app.route("/api/v1.0/pisa")
def pisa():
    pisa_table = db.pisa.find()
    # convert to list
    pisa_table = list(pisa_table)
    print(pisa_table)
    
    return dumps(pisa_table)


@app.route("/api/v1.0/population_english")
def population_english():
    population_english_table = db.population_english.find()
    # convert to list
    population_english_table = list(population_english_table)
    print(population_english_table)
    
    return dumps(population_english_table)


@app.route("/api/v1.0/weather")
def weather():
    weather_table = db.weather.find()
    # convert to list
    weather_table = list(weather_table)
    print(weather_table)
    
    return dumps(weather_table)

@app.route("/api/v1.0/work")
def work():
    work_table = db.work.find()
    # convert to list
    work_table = list(work_table)
    print(work_table)
    
    return dumps(work_table)


if __name__ == "__main__":
    app.run(debug=True)