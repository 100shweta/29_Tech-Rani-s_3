from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('homepg.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/registerhere', methods=['GET', 'POST'])
def registerhere():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

        #return redirect(url_for('/preferences'))
    return render_template('registerhere.html')

@app.route('/preferences')
def preferences():
    return render_template('preferences.html')

@app.route('/company',methods=['GET', 'POST'])
def company():
    if request.method == 'POST':
        company_name = request.form['company_name']
        email_id= request.form['email_id']
        phone_no= request.form['phone_no']
        address= request.form['address']
        HR_name= request.form['HR_name']
        company_web= request.form['company_web']
        industry= request.form['industry']
        required_design= request.form['required_design']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Company (company_name, email_id, phone_no, address, HR_name, company_web, industry, required_design) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (company_name, email_id, phone_no, address, HR_name, company_web, industry, required_design))
        mysql.connection.commit()
        cur.close()

        #return redirect(url_for('/preferences'))

    return render_template('company.html')

@app.route('/employee',methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        Full_name = request.form['Full_name']
        email_id= request.form['email_id']
        phone_no= request.form['phone_no']
        address= request.form['address']
        depart= request.form['depart']
        design= request.form['design']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee ('Full_name', 'email_id, phone_no, address, depart, design) VALUES (%s, %s, %s, %s, %s, %s)", (Full_name, email_id, phone_no, address, depart, design))
        mysql.connection.commit()
        cur.close()
        print('done')
    return render_template('employee.html')



if __name__ == '__main__':
    app.run(debug=True)
