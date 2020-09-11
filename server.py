from flask import Flask ,render_template,request
import datetime

app=Flask(__name__)

products=[
    {
        'titre':"HP 15",
        'image':"2_2.jpg",
        'description':"8 gb ddr4"
    },
    {
        'titre':"ASUS vivabook",
        'image':"3jpg.jpg",
        'description':"8 gb ddr4"
    },
    {
        'titre':"SONY ",
        'image':"4.jpg",
        'description':"8 gb ddr4"
    }   
]

messages = []
@app.route("/")
def home():
	return render_template("home.html", today=datetime.datetime.now().date(), prods=products, titre="Home")
@app.route("/about")
def about():
    return render_template("about.html", today=datetime.datetime.now().date(), titre="About")

@app.route("/contact",methods=['GET','POST'])
def contact():
    valid=False
    if request.method=="POST":
        nom=request.form.get("nom")
        mail=request.form.get("mail")
        message=request.form.get("message")
        msg={'nom':nom, 'mail':mail, 'message':message}
        messages.append(msg)
        valid=True
    return render_template("contact.html", valid=valid, messages=messages)

if __name__=="__main__":
    	app.run(debug=True)
