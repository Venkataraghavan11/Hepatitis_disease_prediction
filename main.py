from flask import Flask, render_template,request
import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/validate',methods=['POST','GET'])
def validate():
    if request.method == 'POST':
        name = request.form.get('username')
        upass = request.form.get('password')
        if name == 'root' and upass == '1234':
            return render_template('index.html')
        else:
            return render_template('login.html',msg='Invalid Data')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        list_ = []
        list_.append(int(request.form.get('age')))
        list_.append(int(request.form.get('gender')))
        list_.append(int(request.form.get('Nausea')))
        list_.append(int(request.form.get('dbreathing')))
        list_.append(int(request.form.get('weight_loss')))
        list_.append(int(request.form.get('weakness')))
        list_.append(int(request.form.get('polyphagia')))
        list_.append(int(request.form.get('genital')))
        list_.append(int(request.form.get('visual')))
        list_.append(int(request.form.get('itching')))
        list_.append(int(request.form.get('irritability')))
        list_.append(int(request.form.get('delay')))
        list_.append(int(request.form.get('Headache')))
        list_.append(int(request.form.get('fever')))
        list_.append(int(request.form.get('cold')))
        list_.append(int(request.form.get('Jaundice')))

        model = joblib.load('model.pkl')
        result = model.predict([list_])
        num = str(result).replace('[','')
        num = str(num).replace(']','')
        
        if num == '1':
            return render_template('out.html',msg='High Risk')
        else:
            return render_template('out.html',msg='Low Risk')

if __name__ == '__main__':
    app.run(debug=True)
