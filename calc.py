from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/numsum")
def numsum(a=-100,b=200):
    c = str(a + b)
    return c


@app.route("/numsub")
def numsub(a=-100,b=300):
    c = str(a-b)
    return c

#if __name__ == __main___:
    #app.run('0.0.0.0',5000)
    
# flask --app calc run