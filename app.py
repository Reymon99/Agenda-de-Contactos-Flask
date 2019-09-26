from flask import Flask
from flask import flash
from flask import render_template as render
from flask import request
from flask import redirect
from flask import url_for
from database import Database

app = Flask(__name__)
app.secret_key = 'mysecretkey'
db = Database()


@app.route('/')
def index():
    return render('index.html', contacts=db.list_contacts())


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        db.add_contact(request.form['fullname'], request.form['phone'], request.form['email'])
        flash('Contact Added Successfully')
        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete(id):
    db.delete_contact(id)
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))


@app.route('/edit/<id>')
def get_contact(id):
    return render('edit_contact.html', contact=db.get_contact(id))


@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        contact = (
            request.form['fullname'],
            request.form['phone'],
            request.form['email'],
            id
        )
        db.update_contact(contact)
        flash('Contact Update Successfully')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
