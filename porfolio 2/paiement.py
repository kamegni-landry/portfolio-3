from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

# Clés API (à obtenir sur Orange Developer)
API_URL = "https://api.orange.com/orange-money-webpay/cm/v1/webpayment"
ACCESS_TOKEN = "TON_ACCESS_TOKEN"  # fourni par Orange
MERCHANT_KEY = "TON_MERCHANT_KEY"  # fourni par Orange

@app.route('/payer', methods=['POST'])
def payer():
    data = request.json
    montant = data.get("montant")
    commande_id = data.get("commande_id")

    payload = {
        "merchant_key": MERCHANT_KEY,
        "currency": "XAF",
        "order_id": commande_id,
        "amount": montant,
        "return_url": "http://127.0.0.1:5000/success",
        "cancel_url": "http://127.0.0.1:5000/cancel"
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        return jsonify({"message": "Lien de paiement généré", "data": response.json()})
    else:
        return jsonify({"error": response.text}), 400

@app.route('/success')
def success():
    return "✅ Paiement réussi, merci pour votre achat !"

@app.route('/cancel')
def cancel():
    return "❌ Paiement annulé."

if __name__ == '__main__':
    app.run(debug=True)
import requests

API_URL = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
ACCESS_TOKEN = "TON_ACCESS_TOKEN"
SUBSCRIPTION_KEY = "TA_SUBSCRIPTION_KEY"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Reference-Id": "ID_TRANSACTION_UNIQUE",
    "X-Target-Environment": "sandbox",
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "Content-Type": "application/json"
}

payload = {
    "amount": "850000",
    "currency": "XAF",
    "externalId": "CMD12345",
    "payer": {"partyIdType": "MSISDN", "partyId": "237677000000"},
    "payerMessage": "Achat iPhone 14 Pro",
    "payeeNote": "Merci pour votre achat"
}

response = requests.post(API_URL, json=payload, headers=headers)
print(response.text)
