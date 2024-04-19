from flask import Flask,render_template
import pandas as pd
import json
import plotly
import plotly.express as px
from datetime import datetime
import time
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Flask(__name__)

def filter_current_month(data):
    data['Month'] = data['Month'].astype(str)
    data['Year'] = data['Year'].astype(str)

    now = datetime.now()
    month = now.strftime("%B")
    year = str(now.year)
    every_this_month = data[(data['Month'] == month) & (data['Year'] == year)]
    return every_this_month

def filter_current_year(data):
    now = datetime.now()
    current_year = now.year
    filtered_data = data[data['Year'] == current_year]
    return filtered_data



def get_table(offset=0, per_page=10):
    return table[offset: offset + per_page]

@app.route('/')
def dashboard():
    data = pd.read_csv('random_data.csv')



    this_year = filter_current_year(data)
    this_month = filter_current_month(data)

    load_figure_template('darkly')

    line = px.line(this_month, x="Date",y="Mood",template='darkly')
    lineJSON = json.dumps(line, cls=plotly.utils.PlotlyJSONEncoder)
    bar = px.histogram(this_year, x="Month",color='Mood',barmode='group',template='darkly')
    barJSON = json.dumps(bar, cls=plotly.utils.PlotlyJSONEncoder)

    mood_per_year = data.groupby('Year')['Mood'].value_counts().reset_index(name='Count')

    year = px.line(mood_per_year, x="Year", y="Count", color='Mood',template='darkly')
    yearJSON = json.dumps(year, cls=plotly.utils.PlotlyJSONEncoder)


    table = data.to_html(classes='table table-striped text-center card-body mt-3',index=False).replace('<tr style="text-align: right;">', '<tr style="text-align: center;">')




    return render_template('index.html',tables=[table],line=lineJSON,bar=barJSON,years=yearJSON,title=[''])


if __name__ == "__main__":
    app.run(host="localhost",port=8129)