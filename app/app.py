import numpy as np
import pandas as pd
import json
import sqlalchemy as db
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template


app = Flask(__name__)

# Create an engine that can talk to the database
engine = db.create_engine('sqlite:///../../data/epi_db.sqlite')
connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)
EF = db.Table('epifactor', metadata, autoload=True, autoload_with=engine)
WL = db.Table('word_list', metadata, autoload=True, autoload_with=engine)

# Select the table to query
query = db.select([EF])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

# Send quesry results from table to a dataframe
ResultSet = pd.DataFrame(ResultSet)

# Drop column "0" and row 0 (not importing index and column names?), resset index to start a 0 and rename columns
ResultSet.drop([0], inplace=True)
ResultSet.drop(0, axis=1, inplace=True)
ResultSet.reset_index(inplace=True)
ResultSet.rename(columns={1:'Calories', 2:'Fat', 3:'Protein', 4:'Ingredients'}, inplace=True)

@app.route('/')
def index():
   
    return render_template('index2.html')

@app.route('/radar')
def radar():
    # df = pd.read_csv('data_1.csv')
    # data = df.to_dict(orient='records')
    data = [{'name': 'Calories', 'value': ResultSet['Calories'][0]},
                   {'name': 'Fat', 'value': ResultSet['Fat'][0]},
                   {'name': 'Protein', 'value': ResultSet['Protein'][0]},
                   {'name': 'Ingredients', 'value': ResultSet['Ingredients'][0]},
                   {'name': 'Nothing', 'value': 0.2}] 
    
    return render_template('radar.html', data=data)   

@app.route('/radar2') 
def radar2():
    # df = pd.read_csv('data_2.csv')
    # data = df.to_dict(orient='records')
    data = [{'name': 'Calories', 'value': ResultSet['Calories'][1]},
                   {'name': 'Fat', 'value': ResultSet['Fat'][1]},
                   {'name': 'Protein', 'value': ResultSet['Protein'][1]},
                   {'name': 'Ingredients', 'value': ResultSet['Ingredients'][1]},
                   {'name': 'Nothing', 'value': 0.2}] 

    return render_template('radar.html', data=data)
@app.route('/radar3') 
def radar3():
    # df = pd.read_csv('data_3.csv')
    # data = df.to_dict(orient='records')
    data = [{'name': 'Calories', 'value': ResultSet['Calories'][2]},
                   {'name': 'Fat', 'value': ResultSet['Fat'][2]},
                   {'name': 'Protein', 'value': ResultSet['Protein'][2]},
                   {'name': 'Ingredients', 'value': ResultSet['Ingredients'][2]},
                   {'name': 'Nothing', 'value': 0.2}] 

    return render_template('radar.html', data=data)   

@app.route('/radar4') 
def radar4():
    # df = pd.read_csv('data_4.csv')
    # data = df.to_dict(orient='records')
    data = [{'name': 'Calories', 'value': ResultSet['Calories'][3]},
                   {'name': 'Fat', 'value': ResultSet['Fat'][3]},
                   {'name': 'Protein', 'value': ResultSet['Protein'][3]},
                   {'name': 'Ingredients', 'value': ResultSet['Ingredients'][3]},
                   {'name': 'Nothing', 'value': 0.2}] 
    
    return render_template('radar.html', data=data)     

@app.route('/radar5') 
def radar5():
    # df = pd.read_csv('data_5.csv')
    # data = df.to_dict(orient='records')
    data = [{'name': 'Calories', 'value': ResultSet['Calories'][4]},
                   {'name': 'Fat', 'value': ResultSet['Fat'][4]},
                   {'name': 'Protein', 'value': ResultSet['Protein'][4]},
                   {'name': 'Ingredients', 'value': ResultSet['Ingredients'][4]},
                   {'name': 'Nothing', 'value': 0.2}] 

    return render_template('radar.html', data=data)

@app.route('/word_cloud')
def word_cloud():
    query = db.select([WL])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    data = ResultSet[0].tolist()
    return render_template('word_cloud.html', data=data)    

if __name__ == "__main__":
    app.run(debug=True)