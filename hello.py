from flask import Flask, render_template
app = Flask(__name__)

#print(dir(Flask));
@app.route("/")
def hello():
	return render_template('webcode.html') 
@app.route("/service")
def hello1():
	return render_template('services.html')
#runnable through python cli  'python hello.py' else use FLASK_APP=hello.py flask run -h localhost -p 3000
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 3005)

