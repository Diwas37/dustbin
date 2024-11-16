from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Path to the wallet file
WALLET_FILE = "wallet.txt"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_last_wallet_amount")
def get_last_wallet_amount():
    try:
        with open(WALLET_FILE, "r") as file:
            # Read all lines and take the last one
            lines = file.readlines()
            last_line = lines[-1].strip() if lines else "0"
            return jsonify({"amount": last_line})
    except FileNotFoundError:
        return jsonify({"amount": "0"})  # Default value if file not found

if __name__ == "__main__":
    app.run(debug=True)
