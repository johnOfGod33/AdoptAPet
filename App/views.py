from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello adopt a pet website'


if __name__=="__main__":
    app.run()