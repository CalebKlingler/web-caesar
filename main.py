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
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height:120px;
            }}
        </style>
    </head>
    <body>
        <form action='/' method="POST">
            <label for="rot">Rotate by: </label>
            <input type="text" name="rot" value="0" />
            <textarea name="text" />{0}</textarea>
            <input type="submit">
        </form>
    </body>
'''
@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encryption():
    rot= int(request.form["rot"])
    text=str(request.form["text"])
    message = str(encrypt(text,int(rot)))
    return form.format(message)




app.run()
