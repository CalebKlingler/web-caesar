from flask import Flask, request
from caesar import encrypt
from helpers import alphabet_position, rotate_character


app=Flask(__name__)
app.config['DEBUG']= True

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height:120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by: </label>
            <input type="text" name="rot" value="0" />
            <textarea name="text" /></textarea>
            <input type="submit">
        </form>
    </body>
'''
@app.route('/')
def index():
    return form

@app.route('/', methods=['POST'])
def encryption():
    rot=request.args.get("rot")
    text=request.args.get("text")
    message = encrypt(text,rot)  
    return "<h1>" + message + "</h1>"




app.run()
