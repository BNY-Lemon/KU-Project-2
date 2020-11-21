from flask import Flask, render_template, jsonify, redirect
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Pass connection to the pymongo instance.
client = pymongo.MongoClient("mongodb://DVGroup3:sealab2021@cluster0-shard-00-00.g3kws.mongodb.net:27017,cluster0-shard-00-01.g3kws.mongodb.net:27017,cluster0-shard-00-02.g3kws.mongodb.net:27017/happiness?ssl=true&replicaSet=atlas-183d98-shard-0&authSource=admin&retryWrites=true&w=majority")

# Connect to a database. Will create one if not already available.
db = client.happiness

# Set route
@app.route('/')
def index():
    # Store the entire happiness collection in a list
    happiness = db.happiness.find_one()
    print(happiness)

    # Return the template with the happiness list passed in
    return render_template('index.html', happiness=happiness)

if __name__ == "__main__":
    app.run(debug=True)