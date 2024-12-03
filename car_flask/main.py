from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('car_purchase.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    prediction=model.predict(np.array([[30,25000]]))

    binary_prediction =1 if prediction[0] =='purchased'else 0

    return render_template("index.html",y="chance of customer to purchase the car "+str(np.round(binary_prediction)))



if __name__ == '__main__' :
    app.run(debug=True)
          
