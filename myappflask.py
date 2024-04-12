from flask import Flask, request

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return "<p>Hola Mundo</p>"

@app.route("/hora")
def hora():
    return "<h1>La hora es: </h1>"

@app.route("/factorial")
def factorial():
    fact = 1
    num = int(request.args.get('num'))
    for x in range(1,num+1):#mas 1 porque range no asume el ultimo valor
        fact *= x
    return str(fact)