from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


#New Ninja
@app.route("/ninjas")
def create_ninja():
    dojo = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos = dojo)


#New Ninja Add To DB
@app.route("/create_ninja", methods=["POST"])
def add_ninja_to_db():
    Ninja.new_ninja(request.form)
    return redirect("/dojos")




