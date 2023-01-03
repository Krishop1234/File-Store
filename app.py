from flask import Flask
app = Flask(__name__)

@app.route('/File_store_Rushidhar_Bot')
def hello_world():
    return redirect("https://telegram.me/File_store_Rushidhar_1Bot", code=302)

if __name__ == "__main__":
    app.run()
