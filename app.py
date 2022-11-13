from flask import Flask, render_template, request
import model as m

app = Flask(__name__,template_folder='template')


@app.route("/",methods=['POST'])
def hello():
    if request.method == "POST":
        Temp = request.form['Temp']
        Press = request.form['Press']
        Rain = request.form['Rain']
        Wind = request.form['Wind']
        pred = m.prediction(Temp,Press,Rain,Wind)
        print(pred)
        
    return render_template("index.html")


# @app.route("/sub",methods=['POST'])
# def submit():
#     if request.method =="POST":
#         name =request.form["username"]

#     return render_template("submit.html",n=name)

if __name__=="__main__":
    app.run(debug=True)