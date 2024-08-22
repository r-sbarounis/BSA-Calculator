from flask import Flask, request, jsonify, render_template
import math



app = Flask(__name__)


        
    


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    h = request.form['h']
    w = request.form['w']
    first_part= int(h) * int(w)
    second_part= first_part/3131
    result= (math.sqrt(second_part))
    rounded_number = round(result,2)

    print('rounded_number')
 

    return render_template('index.html',prediction_text=rounded_number)


if __name__ == "__main__":
    app.run(debug=True)

     