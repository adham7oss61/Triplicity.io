from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    num_people = data.get('num_people')
    if num_people > 10:
        discount = 0.1  # 10% discount for groups of 11 or more
    else:
        discount = 0
    price = 100  # base price per person
    total_price = (price * num_people) * (1 - discount)
    return jsonify({'total_price': total_price})

if _name_ == '_main_':
    app.run(debug=True)
