from flask import Flask, request

app = Flask(__name__)

# Route pour recevoir les données
@app.route("/metasploit", methods=["POST"])
def receive_data():
    data = request.data.decode('utf-8')
    print(f"Données reçues : {data}")
    return "Données reçues avec succès.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
