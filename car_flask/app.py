from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('car_purchase.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   p = request.form["id"]
   q = request.form["gd"]
   r = request.form["as"]
   s = request.form["ps"]
   if (q=="male"):
       q=1
   
   else:
       s=0 

   t =  [[float(p),float(q),float(r),float(s)]] 
   output =model.predict(t)
   print(output)

   return render_template("index.html", y = "The predicted profit is  "+str(np.round(output[0])))

if __name__ == '_main_' :
    app.run(debug=True)