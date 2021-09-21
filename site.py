import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return ("Bot is Connected to Discord")

def site():
	app.run(
		host="0.0.0.0", 
		# The random port is for the reason that sometimes the default port 8080 is already in use
		port=random.randint(2000, 9000)
	)

site()