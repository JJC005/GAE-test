from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, abort
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
#from passlib.hash import sha256_crypt
#from functools import wraps
app = Flask(__name__)

#START MY CODE*****************************************************************************************************************************
# Index
@app.route('/')
def index():
    return render_template('home.html')

#Will complete for Login page
@app.route('/login', methods=['POST'])
def do_login():
 
POST_USERNAME = str(request.form['username'])
POST_PASSWORD = str(request.form['password'])
 
Session = sessionmaker(bind=engine)
s = Session()
query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
result = query.first()
if result:
session['logged_in'] = True
else:
flash('wrong password!')
return home()
#End do_login

# Will complete for Password Reset
@app.route('/passwordReset')
def pwReset():
    return render_template('psReset.html')

# Will complete for League Page. This is the main hub once logged in
@app.route('/league')
def league():
    return render_template('league.html')

# Will complete for Tier Details. This will be linked from the appropriate tier, based on tier # and squad
@app.route('/tierDetails')
def tierDetails():
    return render_template('tierDetails.html')

# Will complete for Drop/Add. This will be linked from the appropriate tier, squad
@app.route('/dropAdd')
def dropAdd():
    return render_template('dropAdd.html')

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
