from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome' + ' ' + name + '!'

if __name__ == '__main__':
    app.run(debug=True)
