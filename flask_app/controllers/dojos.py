from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

#Dojos
@app.route("/dojos")
def create_dojo():
    
    return render_template("index2.html", all_dojos = Dojo.get_all_dojos())

#New Dojo Add To DB
@app.route("/create_dojo", methods=["POST"])
def add_dojo_to_db():
    Dojo.new_dojo(request.form)
    return redirect("/dojos/<int:dojo_id")


#Show Dojo
@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    
    this_dojo = Dojo.get_ninjas_in_dojo({"id": dojo_id})
    
    return render_template("index3.html", dojo = this_dojo)



