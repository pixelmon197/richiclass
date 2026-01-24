from flask import *

def app():
    app = Flask(__name__)
    @app.route('/')
    
    def home():
        return "Hola mundo"
    
    return app
    
app = app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)