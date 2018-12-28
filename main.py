from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
#from passlib.hash import sha256_crypt
#from functools import wraps
app = Flask(__name__)

#START MY CODE*****************************************************************************************************************************
# Index
@app.route('/')
def index():
    return render_template('home.html')

#Will complete for login page
@app.route('/login')
def login():
    return 'This is where the login page goes'

# Check if user logged in
#def is_logged_in(f):
   # @wraps(f)
    #def wrap(*args, **kwargs):
     #   if 'logged_in' in session:
      #      return f(*args, **kwargs)
       # else:
        #    flash('Unauthorized, Please login', 'danger')
         #   return redirect(url_for('login'))
   # return wrap

# Logout
#@app.route('/logout')
#@is_logged_in
#def logout():
 #   session.clear()
  #  flash('You are now logged out', 'success')
   # return redirect(url_for('login'))

#END MY CODE*******************************************************************************************************************************

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
