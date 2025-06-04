# Python Math Library and Web Application

This project provides a Python library with number theory functions and a web application to interact with them. It also includes a command-line tool specifically for exploring Goldbach's conjecture.

## Project Structure

-   `pymath/`: Directory containing the core mathematical library.
    -   `lib.py`: The main library file with mathematical functions.
    -   `tests/`: Directory for unit tests.
        -   `test_lib.py`: Unit tests for the functions in `lib.py`.
-   `cli_app.py`: A command-line application to check Goldbach's conjecture for a range of numbers.
-   `webapp.py`: A Flask web application that exposes the math library functions via an API.
-   `README.md`: This file.

## Features

### Mathematical Library (`pymath/lib.py`)

The library currently includes the following functions:

-   `is_prime(n)`: Checks if an integer `n` is a prime number.
-   `check_goldbach(n)`: Checks if an even integer `n > 2` can be expressed as the sum of two prime numbers. Returns the pair of primes if found, otherwise `None`.
-   `gcd(a, b)`: Calculates the Greatest Common Divisor (GCD) of two integers `a` and `b`.
-   `lcm(a, b)`: Calculates the Least Common Multiple (LCM) of two integers `a` and `b`.
-   `factorial(n)`: Calculates the factorial of a non-negative integer `n`.

### Command-Line Application (`cli_app.py`)

This tool allows you to check Goldbach's conjecture for a range of even numbers.

**Usage:**

1.  Navigate to the project directory.
2.  Run the script:
    ```bash
    python cli_app.py
    ```
3.  Follow the prompts to enter the starting and ending even numbers.

### Web Application (`webapp.py`)

The Flask web application provides API endpoints for the math functions.

**Prerequisites:**

-   Python 3
-   Flask (`pip install Flask`)

**Running the Web App:**

1.  Navigate to the project directory.
2.  Ensure Flask is installed:
    ```bash
    pip install Flask
    ```
3.  Run the web application:
    ```bash
    python webapp.py
    ```
4.  The application will typically start on `http://127.0.0.1:5000/` or `http://0.0.0.0:5000/`.

**Available API Endpoints:**

-   `GET /`: Shows a welcome message with links to available endpoints.
-   `GET /is_prime/<int:number>`: Checks if `<number>` is prime.
    -   Example: `/is_prime/7`
    -   Returns JSON: `{"number": 7, "is_prime": true}`
-   `GET /check_goldbach/<int:number>`: Checks Goldbach's conjecture for an even `<number>` > 2.
    -   Example: `/check_goldbach/10`
    -   Returns JSON: `{"number": 10, "is_goldbach_pair": true, "pair": [3, 7]}` or an error for invalid input.
-   `GET /gcd/<int:num1>/<int:num2>`: Calculates GCD of `<num1>` and `<num2>`.
    -   Example: `/gcd/48/18`
    -   Returns JSON: `{"num1": 48, "num2": 18, "gcd": 6}`
-   `GET /lcm/<int:num1>/<int:num2>`: Calculates LCM of `<num1>` and `<num2>`.
    -   Example: `/lcm/4/6`
    -   Returns JSON: `{"num1": 4, "num2": 6, "lcm": 12}`
-   `GET /factorial/<int:number>`: Calculates factorial of `<number>`.
    -   Example: `/factorial/5`
    -   Returns JSON: `{"number": 5, "factorial": 120}` or an error for negative input.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
(Assuming MIT License based on the original README for Goldbach conjecture part. If different, this should be updated.)
