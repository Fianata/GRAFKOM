from flask import Flask, render_template_string # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<h1>Hello, World!</h1>')

if __name__ == '__main__':
    app.run(debug=True)

