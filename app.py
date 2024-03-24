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

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
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
        qualifications=request.form['qualifications']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee (Full_name,email_id, phone_no, address, depart, design, qualifications) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Full_name, email_id, phone_no, address, depart, design, qualifications))
        mysql.connection.commit()
        cur.close()
    return render_template('employee.html')

@app.route('/it')
def it():
    return render_template('it.html')

@app.route('/finance')
def finance():
    return render_template('finance.html')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/itcom')
def itcom():
    return render_template('itcom.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
