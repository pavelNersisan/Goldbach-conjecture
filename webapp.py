from flask import Flask, jsonify, request
from pymath.lib import is_prime, check_goldbach, gcd, lcm, factorial

app = Flask(__name__)

@app.route('/')
def home():
    # Provide links to the available functions
    return '''
        <h1>Math Web App</h1>
        <p>Use the following endpoints to perform calculations:</p>
        <ul>
            <li><code>/is_prime/&lt;int:number&gt;</code></li>
            <li><code>/check_goldbach/&lt;int:number&gt;</code> (for even numbers > 2)</li>
            <li><code>/gcd/&lt;int:num1&gt;/&lt;int:num2&gt;</code></li>
            <li><code>/lcm/&lt;int:num1&gt;/&lt;int:num2&gt;</code></li>
            <li><code>/factorial/&lt;int:number&gt;</code></li>
        </ul>
    '''

@app.route('/is_prime/<int:number>')
def route_is_prime(number):
    return jsonify(number=number, is_prime=is_prime(number))

@app.route('/check_goldbach/<int:number>')
def route_check_goldbach(number):
    if number <= 2 or number % 2 != 0:
        return jsonify(error="Input must be an even integer greater than 2", number=number), 400
    result = check_goldbach(number)
    if result:
        return jsonify(number=number, is_goldbach_pair=True, pair=result)
    else:
        # This case should ideally not be reached if input validation is done above,
        # but as a fallback for the function's own logic for unrepresentable numbers.
        return jsonify(number=number, is_goldbach_pair=False, message=f"{number} could not be represented as a sum of two primes by this check.")

@app.route('/gcd/<int:num1>/<int:num2>')
def route_gcd(num1, num2):
    return jsonify(num1=num1, num2=num2, gcd=gcd(num1, num2))

@app.route('/lcm/<int:num1>/<int:num2>')
def route_lcm(num1, num2):
    result_lcm = lcm(num1, num2)
    return jsonify(num1=num1, num2=num2, lcm=result_lcm)

@app.route('/factorial/<int:number>')
def route_factorial(number):
    if number < 0:
        return jsonify(error="Factorial is not defined for negative numbers", number=number), 400
    try:
        # The factorial function itself raises ValueError, but for a web API,
        # it's good to also catch it and return a clean JSON response.
        # The check above handles negative numbers specifically for a clearer error message.
        result = factorial(number)
        return jsonify(number=number, factorial=result)
    except ValueError as e: # Should only be for n < 0, already handled, but as a safeguard.
        return jsonify(error=str(e), number=number), 400

if __name__ == '__main__':
    # Note: In a production environment, you would use a WSGI server like Gunicorn or Waitress.
    # The Flask development server is for development purposes only.
    app.run(debug=True, host='0.0.0.0', port=5000)
