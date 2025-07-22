from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html', name='Home')

if __name__=="__main__":
    app.run(debug=True)
    
