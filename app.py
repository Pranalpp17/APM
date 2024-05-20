from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user database
users = {'admin': {'password': 'admin'}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dynamic_form'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/form', methods=['GET', 'POST'])
@login_required
def dynamic_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)  # Handle the form data as needed
        return redirect(url_for('dynamic_form'))
    return render_template('form.html')

@app.route('/results')
@login_required
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
