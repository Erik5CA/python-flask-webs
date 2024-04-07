from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST']  = 'localhost'
app.config['MYSQL_USER']  = 'root'
app.config['MYSQL_PASSWORD']  = 'password'
app.config['MYSQL_DB']  = 'flaskcontacts'
mysql = MySQL(app)

# Settings

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO contacts (fullname, phone, email) VALUES ('{fullname}','{phone}','{email}')")
        mysql.connection.commit()
        flash('Contact added successfully')
        
        return redirect(url_for('index'))
    

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT * FROM contacts WHERE id = {id}')
    data = cur.fetchone()
    print(data)
    return render_template('edit_contact.html', contact = data)

@app.route('/update/<id>', methods= ['POST'])
def update_contact(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur.execute(f"""
                    UPDATE contacts
                    SET fullname = '{fullname}',
                        phone = '{phone}',
                        email = '{email}'
                    WHERE id = {id}
                    """)
        mysql.connection.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute(f'DELETE FROM contacts WHERE id = {id}')
    mysql.connection.commit()
    flash('Contact deleted successfully!')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port = 3000, debug = True)

