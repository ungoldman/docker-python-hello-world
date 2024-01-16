from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/types')
def data_types():
    str = 'quarks'
    num = 42
    flt = 2.3
    lst = [str, num, flt]
    # no shorthand notation in python
    dct = {
        'string': str,
        'number': num,
        'float': flt,
        'list': lst
    }
    return {
        'dictionary': dct
    }

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5001)
