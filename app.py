from flask import Flask, render_template, session, url_for, request, redirect, escape
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'leyni'

vorur = [   [0,"Arnar","arnar.jpg",],
            [1,"Guðjón","gudjon.jpg",],
            [2,"Ágúst","agust.jpg",500],
            [3,"Lorraine","lorraine.jpg",350],
            [4,"Wiktor","wiktor.jpg",300],
            [5,"Oskar","oskar.jpg",500],]


@app.route("/")
def index():
    karfa=[]
    fjoldi=0
    if 'karfa' in session:
        karfa=session['karfa']
        fjoldi=len(karfa)
    return render_template("index.tpl", v=vorur, fjoldi=fjoldi)

@app.route("/add/<int:id>")
def frett(id):
    karfa=[]
    fjoldi=0
    if 'karfa' in session:
        karfa=session['karfa']
        karfa.append(vorur[id])
        session['karfa']=karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur[id])
        session['karfa']=karfa
        fjoldi = len(karfa)
    
    return f'<head><meta http-equiv="Refresh" content="0; url=/#item{id}"></head>'

@app.route("/karfa")
def karfa():
    karfa = []
    summa=0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
        for i in karfa:
            summa += int(i[3])
        return render_template("karfa.tpl", k=karfa, tom=False, fjoldi=fjoldi, samtals=summa)
    else:
        return render_template("karfa.tpl", k=karfa, tom=True)

@app.route("/eydavoru/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session["karfa"]
    index=0
    for i in range(len(karfa)):
        if karfa[i][0] == id:
            index = i
    karfa.remove(karfa[index])
    session["karfa"] = karfa
    return render_template("eydavoru.tpl")

@app.route("/eyda")
def eyda():
    session.pop("karfa", None)
    return render_template("eyda.tpl")

@app.route("/result", methods = ["POST","GET"])
def result():
    if request.method == "POST":
        kwargs={
            "name": request.form["nafn"],
            "email": request.form["email"],
            "phone": request.form["simi"],
            "price": request.form["samtals"],
        }
        return render_template("result.tpl",**kwargs)

@app.route("/logout",methods = ["GET","POST"])
def logout():
    session.pop("karfa", None)
    return redirect(url_for("index"))

@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.tpl"),404

@app.errorhandler(405)
def not_allowed(error):
    return render_template("not_allowed.tpl"),405

if __name__ == '__main__':
    app.run(debug=True)