from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    from eventlet import wsgi, listen
    wsgi.server(listen(('0.0.0.0', int(os.getenv("PORT", default=50000)))), app)

