from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_f_to_c():
    # Check if "fahrenheit" is in the query string
    if 'fahrenheit' in request.args:
        fahrenheit = float(request.args['fahrenheit'])
        celsius = (fahrenheit - 32) * 5/9
        return jsonify({
            #'Fahrenheit given': fahrenheit,
            'Celsius': celsius
        }), 200
    else:
        return "Error: No fahrenheit field provided. Please specify an amount.", 400

if __name__ == '__main__':
    app.run(debug=True)
