# Fazendo connection do Flask com Python na Web


from flask import Flask

app =  Flask(__name__)

@app.route("/")

def index():
    return "Olá mundo"

if __name__ == "__main__":
    app.run()