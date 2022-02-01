from flask import Flask, render_template
import sys

file = sys.argv[1]

print("click ctrl+c when you have viewed the 127.0.0.1:5000 to continue ^^")

app = Flask(__name__, template_folder="../")

@app.route("/")
def index():
	return render_template(file)

if "__main__" == __name__:
	app.run()
