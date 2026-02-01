from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/form")
def form():
    return render_template("form.html")
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form["username"]
    branch=request.form["branch"]
    return render_template("result.html",Name=name,Branch=branch)

if __name__=="__main__":
    app.run(debug=True)