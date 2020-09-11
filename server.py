from flask import Flask ,render_template
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


@app.route("/")
def home():
	return render_template("home.html", today=datetime.datetime.now().date(), prods=products, titre="Home")
@app.route("/about")
def about():
    return render_template("about.html", today=datetime.datetime.now().date(), titre="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", today=datetime.datetime.now().date(), titre="Contact")

if __name__=="__main__":
    	app.run(debug=True)
