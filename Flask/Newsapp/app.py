from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/news/<id>')
def news(id):
    id=id
    return render_template('{}.html'.format(str(id)))


    

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")