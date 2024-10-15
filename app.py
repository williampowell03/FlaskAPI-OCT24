from flask import Flask, request, jsonify

app = Flask(__name__)

drug_inventory = [
    {"id": 1, "name": "Aspirin", "quantity": 50},
    {"id": 2, "name": "Paracetamol", "quantity": 100},
    {"id": 3, "name": "Amoxicillin", "quantity": 75}
]
#GET API method
@app.route('/drugs', methods=['GET'])
def get_drugs():
    return jsonify(drug_inventory)


#POST API method
@app.route('/drugs', methods=['POST'])
def add_drug():
    new_drug = request.json
    new_drug["id"] = len(drug_inventory) + 1
    drug_inventory.append(new_drug)
    return jsonify(new_drug), 201

#PUT API method
@app.route('/drugs/<int:drug_id>', methods=['PUT'])
def update_drug(drug_id):
    updated_data = request.json
    for drug in drug_inventory:
        if drug['id'] == drug_id:
            drug['name'] = updated_data.get('name', drug['name'])
            drug['quantity'] = updated_data.get('quantity', drug['quantity'])
            return jsonify(drug), 200
    return jsonify({"message": "Drug not found"}), 404

@app.route('/drugs/<int:drug_id>', methods=['DELETE'])
def delete_drug(drug_id):
    global drug_inventory
    drug_inventory = [drug for drug in drug_inventory if drug['id'] != drug_id]
    return jsonify({"message": "Drug deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
