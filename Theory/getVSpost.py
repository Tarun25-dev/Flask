"""
GET vs POST:

GET: Used to get / read data from server
     Data is visible in URL
     safe for searching

Example URL:
/search?item=phone

@app.route("/hello")
def hello():
    return "Hello World"
>> Browser does a GET request automatically.

POST: Used to send data to a server
      Data is hidden from URL
      Used for forms, passwords, login
Example:
>> Login form
>> Signup form
>> Payment form

simple logic understanding example:
>> Think of a Website Like a Shop
   >> You = customer
   >> Flask server = shop owner
>> There are two main ways you talk to the shop owner:
   >> Asking something
   >> Giving something
   thats GET and POST
"""