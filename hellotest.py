from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/aboutUs')
def aboutUs():
    return render_template("aboutUs.html")

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome' + ' ' + name + '!'

if __name__ == '__main__':
     server.run(host = '0.0.0.0',port = 80)
