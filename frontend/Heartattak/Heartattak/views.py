"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,flash
from Heartattak import app , tree as t

app.secret_key = "supandi"
@app.route('/',methods=["POST","GET"])
def home():
    data = {'age':0,'sex':0,'cp':0,'trestbps':0,'chol':0,'fbs':0,'restecg':0,
        'thalach':0,'exang':0,'oldpeak':0,'slope':0,'ca':0,'thal':0}
    if request.method == "POST":
        #data["age"] = request.form["age"]
        #data["sex"] = request.form["sex"]
        #data["cp"] = request.form["cp"]
        #data["trestbps"] = request.form["trestbps"]
        #data["chol"] = request.form["chol"]
        #data["fbs"] = request.form["fbs"]
        #data["restecg"] = request.form["restecg"]
        #data["thalach"] = request.form["thalach"]
        #data["exang"] = request.form["exang"]
        #data["oldpeak"] = request.form["oldpeak"]
        #data["slope"] = request.form["slope"]
        #data["ca"] = request.form["ca"]
        #data["thal"] = request.form["thal"]
        for i in data:
            data[i] = float(request.form[i])
       
        color = (t.tree(data, 0, 0))
        print(color)
        if color == 0:
            color = "green"
            msg = "You have low risk of heart condition"

        elif color == 1:
            color = "red"
            msg = "You have high risk of heart condition"
        
        flash(msg,"info")    
        return render_template('index2.html',title='Home Page',color = color)
        

    
    
        
        
    else:
        color = "black"
        return render_template('index.html',title='Home Page',color = color)

