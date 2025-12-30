from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
# Initialize SQLAlchemy. We'll call create_all() after the models are defined
# so SQLAlchemy knows about `FirstApp` when it creates tables.
db = SQLAlchemy(app)


class FirstApp(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.fname}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')

        if fname and lname and email:
            firstapp = FirstApp(fname=fname, lname=lname, email=email)
            db.session.add(firstapp)
            db.session.commit()

    #     print(request.form['fname'])

    # firstapp = FirstApp(fname="Azan", lname="Khan", email="azan.khan@example.com")
    # db.session.add(firstapp)
    # db.session.commit()

    allpeople = FirstApp.query.all()
    return render_template("index.html", allpeople=allpeople)

    return render_template("index.html", allpeople=allpeople)

@app.route("/home")
def home():
    return "<p>Welcome to the Home Page!</p>"


@app.route("/delete/<int:sno>", methods=['POST'])
def delete_person(sno):
    person = FirstApp.query.get_or_404(sno)
    db.session.delete(person)
    db.session.commit()
    return render_template("index.html", allpeople=FirstApp.query.all())

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update_person(sno):
    person = FirstApp.query.get_or_404(sno)
    if request.method == 'POST':
        person.fname = request.form.get('fname')
        person.lname = request.form.get('lname')
        person.email = request.form.get('email')
        db.session.commit()
        return redirect(url_for('hello_world'))
    return render_template("update.html", person=person)

# Create the database tables after model definitions so they exist at runtime.
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
