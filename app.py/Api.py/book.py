from flask import Flask, request, jsonify

app = Flask(__GroupDiscount_)

@app.route('/book', methods=['POST'])
def book():
  # ... your booking logic with discount calculation based on num_people
  return jsonify({'total_price': total_price})

if __GroupDiscount_ == '__main__':
  app.run(debug=True)
