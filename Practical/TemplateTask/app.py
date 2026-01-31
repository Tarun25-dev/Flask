from flask import Flask,render_template 
# render_template is a function that allows Flask to send HTML files to the user.
app=Flask("__name__")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/user")
def user():
    name="Tharun Kumar"
    return render_template("index.html",username=name)# that username will use in index html file.
@app.route("/profile")
def profile():
    sname="Tharun Kumar K"
    branch="CSD"
    year=2022
    return render_template("index.html",sn=sname,b=branch,y=year)
if __name__=="__main__":
    app.run(debug=True)