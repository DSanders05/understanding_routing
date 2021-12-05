from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def route():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {str(name)}'

@app.route('/repeat/<num>/<word>')
def repeat_word(num,word):
    message = ''
    for words in range(int(num)):
        message += word + " "
    return message

if __name__=="__main__":    
    
    app.run(debug=True)

