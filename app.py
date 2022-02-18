from flask import Flask, request, render_template
#import requests
import sklearn
import pickle
import pandas as pd
import numpy as np
app = Flask(__name__)

model = pickle.load(open("Students_Placed_Logistic_SC_new.pkl", "rb"))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        cgpa = float(request.form["cgpa"])
        iq = int(request.form["iq"])
        profile_score = int(request.form["profile_score"])
       
        #prediction = model.predict(pd.DataFrame([[cgpa,iq,profile_score]],columns=['cgpa','iq','profile_score']))
        prediction = model.predict(pd.DataFrame([[cgpa,iq,profile_score]],columns=['cgpa','iq','profile_score']))
        print(prediction)
        if prediction[0] == 0:
            return render_template('index.html',prediction_text="Sorry to say, You have not been Placed")
        elif prediction[0] == 1:
            return render_template('index.html',prediction_text="Congratulation,You have been Placed")

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)








            

        
        
        




    

