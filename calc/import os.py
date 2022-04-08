import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def main():

    return render_template('template.html')

@app.route('/calculadora', methods=['POST','GET'])

def seg():
    getRequest = request.form.get
    valor1 = getRequest('v1')
    valor2 = getRequest('v2')
    operacao = request.form ['operacao']    
    if valor1 and valor2:
        if operacao == '1':
            return jsonify(float(valor1) + float(valor2))
        elif operacao == '2':
            return jsonify(float(valor1) - float(valor2))
        elif operacao == '3':
            return jsonify(float(valor1) / float(valor2))
        elif operacao == '4':
            return jsonify(float(valor1) * float(valor2))
        else:
            return 'error'
    else:
        return 'error'

if __name__ == "__main__":
    app.run(host='localhost',port=5002, debug=True)
