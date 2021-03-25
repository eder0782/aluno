from flask import Flask
from flask import Flask
import time
import contador 

app = Flask(__name__)

@app.route("/")
def inex():

    #contador.contar()
    return 'ola mundo'
    contador.contar()


    
if __name__ == "__main__":
    app.run() 



