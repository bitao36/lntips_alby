from flask import Flask, request, jsonify, render_template
import requests
from decouple import config
app = Flask(__name__)

# Configura tu API key de GetAlby
API_KEY = config('API_KEY')
GETALBY_URL = config('GETALBY_URL')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invoice', methods=['POST'])
def create_invoice():

    
    amount_sat = request.json.get('amount')
    
    if not amount_sat:
        return jsonify({'error': 'Amount is required'}), 400

    try:
        # Convierte amount_sat a entero
        amount_sat = int(amount_sat)
    except ValueError:
        return jsonify({'error': 'Amount must be an integer'}), 400

    # Crear el payload para la API de GetAlby
    data = {
        'amount': amount_sat,
        'description': 'New Tip'
    }

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    try:        
        response = requests.post(f'{GETALBY_URL}invoices', json=data, headers=headers)        
        response_data = response.json()

        if response.status_code == 201:
            return jsonify({
                'payment_request': response_data.get('payment_request'),
                'r_hash': response_data.get('payment_hash')
            })
        else:
            return jsonify({'error': response_data.get('error', 'Unknown error')}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/check_payment/<r_hash>', methods=['GET'])
def check_payment(r_hash):    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(f'{GETALBY_URL}invoices/{r_hash}', headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            state = response_data.get('state')
             
            if state == 'SETTLED':
                return jsonify({'settled': True, 'state': 'PAID'})
            elif state == 'CREATED':
                return jsonify({'settled': False, 'state': 'PENDING'})
            elif state == 'CANCELED':
                return jsonify({'settled': False, 'state': 'CANCELED'})
            else:
                return jsonify({'settled': False, 'state': state })
        else:
            return jsonify({'error': response_data.get('error', 'Unknown error')}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

