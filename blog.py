from flask import Flask, render_template, request, redirect, url_for, flash,session,logging # flaskın kendisi zaten
from flask_mysqldb import MySQL # mysql için
from wtforms import Form, StringField, TextAreaField, PasswordField, validators # form için
from passlib.hash import sha256_crypt # şifreleme için
from functools import wraps # decorator için

# Kullanıcı kaydı
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords not same ')
    ])
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    

app = Flask(__name__)
app.secret_key = "blog"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



mysql = MySQL(app)

#kullanıcı giriş Decoratorı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("login yapın","danger")
            return redirect(url_for("login"))
    return decorated_function

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles')
def articles():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From articles"
    result = cursor.execute(sorgu)
    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html", articles = articles)
    else:
        return render_template("articles.html")


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.hash(str(form.password.data))
        cursor = mysql.connection.cursor()
        sorgu = "Insert into user(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("You are registered","success")
        return redirect(url_for('login'))
    else:
            return render_template("register.html", form = form)
            
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data
        cursor = mysql.connection.cursor()
        sorgu = "Select * From user where username = %s"
        result = cursor.execute(sorgu,(username,))
        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"] 
            if sha256_crypt.verify(password_entered,real_password):
                flash("Success Bro","success")
                session["logged_in"] = True # session oluşturduk,kontrol için kullanacağız
                session["username"] = username #aynı şekilde bir de username oluşturduk
                return redirect(url_for('index'))
            else:
                flash("Password false","danger")
                return redirect(url_for('login'))
        else:
            flash("Böyle biri yok","danger")
            return redirect(url_for('login'))
     
    return render_template("login.html", form = form)
@app.route('/logout')
def logout():
    session.clear() # sessionu sildik
    return redirect(url_for('index'))

#Makale ekleme
@app.route('/addarticle', methods=['GET', 'POST'])
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data
        cursor = mysql.connection.cursor()
        sorgu = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit() # veritabanına kaydetmek için
        cursor.close()
        flash("Başarıyla eklendi","success")
        return redirect(url_for('dashboard'))
    return render_template("addarticle.html", form = form)

#makale form
class ArticleForm(Form):
    title = StringField('Article Title', [validators.Length(min=3, max=100)])
    content = TextAreaField('Article Content', [validators.Length(min=5)])
if __name__ == '__main__':
    app.run(debug=True)
