from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return '<h1>About Page</h1>'

# Form handling route
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
