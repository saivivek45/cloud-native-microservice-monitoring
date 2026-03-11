from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def location():
	data = {
		"classroom" : "batch 2 2023",
		"latitude"  : "9.75505",
		"longitude" : "76.6507"
	       }
	return jsonify(data)

if __name__=="__main__":
	app.run(host="0.0.0.0",port=5000)
