from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Rushidhar1999"

@app.route('/File_store_Rushidhar_Bot')
def redirected():
    return redirect("https://telegram.me/File_store_Rushidhar_1Bot", code=302)

if __name__ == "__main__":
    app.run()
