"""
Route - A route connects URL to a function

Route = URL path + what should happen when user visits it
Example:
URL: http://localhost:5000/
Action: show home page

Without routes:

Flask wouldn't know which page to show
Every URL would be meaningless

simple Example code:

@app.route("/path")
def function_name():
    return response

@app.route("/")
This is a decorator
It registers a URL with Flask
"/" = home page

path may vary according to user wants to show which page like

/	    Calls home()
/about	Calls about()
/login	Calls login()

Example with multiple routes

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

"""