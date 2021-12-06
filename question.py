from flask import Flask,render_template,request
from flask import Flask
from jinja2 import Markup
from flask import  Flask,render_template,jsonify,redirect,url_for
import random
import pandas as pd
df = pd.read_csv('urls.csv')
print(df)

app = Flask(__name__)
idx = 0

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('120114341525.html')
 
@app.route("/question")
def question():
    global idx 
    idx = idx + 1
    df = pd.read_csv('urls.csv')
    print(idx,df.last_valid_index())
    if idx > df.last_valid_index():
        idx =0

    url = df.loc[idx,'url']
    return render_template("index.html",url =url )
if __name__ =="__main__":
    app.run()


