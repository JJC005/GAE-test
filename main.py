from flask import Flask
app = Flask(__name__)
@app.route('/')

#START MY CODE*****************************************************************************************************************************

def hello():
    return 'Only Joey should be able to see this'

#END MY CODE*******************************************************************************************************************************

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
