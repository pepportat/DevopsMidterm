from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hi! from actions - version 1 '

@app.route('/')
def home():
    return '''
        <form action="/greet" method="post">
            <input name="name">
            <input type="submit">
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f"Hello, {name}!"

# es dasatestad chavamate axla, araferi shemicvlia proeqtshi
if __name__ == "__main__":
    app.run()