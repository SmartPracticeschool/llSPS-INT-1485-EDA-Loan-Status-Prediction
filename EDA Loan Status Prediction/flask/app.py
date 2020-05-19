# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:38:28 2020

@author: adida
"""

from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('loan_status.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login',methods =['POST'])
def login():
    g = request.form['G']
    m = request.form['M']
    de = request.form['de']
    ed = request.form['ed']
    se = request.form['se']
    ai = request.form['aincome']
    coai = request.form['coaincome']
    loanamt = request.form['loanamt']
    laterm = request.form['laterm']
    ch = request.form['ch']
    pa = request.form['pa']
    if(g == "Male"):
        g1 = 0
    else:
        g1 = 1
    if(m == "Yes"):
        m1 = 1
    else:
        m1 = 0
    if(de == "0"):
        de1,de2,de3,de4 = 1,0,0,0
    elif(de == "1"):
        de1,de2,de3,de4 = 0,1,0,0
    elif(de == "2"):
        de1,de2,de3,de4 = 0,0,1,0
    elif(de == "3"):
        de1,de2,de3,de4 = 0,0,0,1
    if(ed == "yes"):
        ed1 = 0
    else:
        ed1 = 1
    if se=="yes":
        se1 = 1
    else:
        se1 = 0
    if pa=="r":
        pa1,pa2,pa3 = 1,0,0
    elif pa=="s":
        pa1,pa2,pa3 = 0,1,0
    elif pa=="u":
        pa1,pa2,pa3 = 0,0,1
        
    total = [[pa1,pa2,pa3,de1,de2,de3,de4,g1,m1,ed1,se1,int(ai),float(coai),float(loanamt),float(laterm),float(ch)]]
    print(total)
    y_pred = model.predict(np.array(total))
    
    print(y_pred)
    if y_pred[0] == 1:
        return render_template("index.html",showcase ="loan can be sanctioned ")
    else:
        return render_template("index.html",showcase ="loan cannot be sanctioned")
    


if __name__ == '__main__':
    app.run(debug = True)
