from flask import Flask, request, session, jsonify

app = Flask(__name__)
app.secret_key = "super_secret_key" # Required for session management

# Mock database of bank accounts
accounts = {
    "101": {"name": "Alice (You)", "balance": 5000, "account_type": "Checking"},
    "102": {"name": "Bob (Target)", "balance": 150000, "account_type": "Savings"}
}

@app.route('/login')
def login():
    # Simulate logging in as Alice (User 101)
    session['user_id'] = "101"
    return "Logged in as Alice. <a href='/view_account?id=101'>View My Account</a>"

@app.route('/view_account')
def view_account():
    # VULNERABLE: Takes the 'id' from the URL without checking who is logged in
    account_id = request.args.get('id')

    if account_id in accounts:
        return jsonify(accounts[account_id])
    return "Account not found", 404

if __name__ == '__main__':
    app.run(debug=True)

    #http://127.0.0.1:5000/login