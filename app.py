from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html', name='Home')
@app.route('/contact')
def contact():
    return render_template('contact.html', name='contact')

if __name__=="__main__":
    app.run(debug=True)
    
