from flask import Flask, render_template, request
import requests
import pickle 
import numpy as np 
import sklearn 
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=["GET"])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Year = int(request.form['Year'])
        Owner= int(request.form['Owner'])
        Fuel_Type_Diesel=request.form['Fuel_Type_Diesel']
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        Seller_Type_Individual=request.form['Seller_Type_Individual'
        Transmission_Manual = request.form['Transmission_Manual']

prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))


if __name__=="__main__":
    app.run(debug=True)