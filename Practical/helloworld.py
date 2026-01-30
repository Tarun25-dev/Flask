from flask import Flask # importing Flask class from the flask package.
app=Flask(__name__) # creating a Flask application object.
"""
Why __name__?
If this file is run directly → __name__ == "__main__"
If imported → Flask knows it's a module
"""
@app.route("/")
# This is a decorator.
# It tells Flask:
# When a user opens http://localhost:5000/
# Run the function written just below this line
# / means Root URL
def home(): # This defines a function named home.Flask will call this function when the / route is accessed.
    return "Welcome to Flask!"
if __name__ == "__main__": # Prevents Flask from auto-running when imported into another file.
    app.run(debug=True) # Starts the Flask development server
    
"""debug=True means:
Auto-restart when code changes
Shows detailed error messages
Very useful while learning
 """