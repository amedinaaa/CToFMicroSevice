from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_f_to_c():
    # Check if "fahrenheit" is in the query string
    fahrenheit = request.args.get('fahrenheit')
    if fahrenheit is None:
        return "Error: Please specify an amount.", 400
        
    try: 
        fahrenheit_value = float(fahrenheit)
    except ValueError:
        return "Error: invalid value for fahrenheit. Please provide a valid number", 400
        
    celsius = (fahrenheit_value - 32) * 5/9
    return jsonify({
            #'Fahrenheit given': fahrenheit,
            'Celsius': celsius
        }), 200

if __name__ == '__main__':
    app.run(debug=True)
