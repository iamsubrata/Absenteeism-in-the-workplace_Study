import flask
from flask import request
app=flask.Flask(__name__)
app.config['DEBUG']=True
#from flask_cors import CORS
#CORS(app)

@app.route('/')
def default():
    return '<h1> API server is working </h1>'

@app.route('/predict')

def predict():
    import joblib
    model=joblib.load('Absent_Hour_Predictor_model.ml')
    absent_hrs_predict=model.predict([[26,36,30]])
    
    return str(absent_hrs_predict)

#if deploying in cloud use below IP
if __name__=="__main__":
    
    app.run(debug=True)

#app.run(debug=True);