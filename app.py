from flask import Flask, render_template, json
import os
# import database.db_connector as db

# Configuration

app = Flask(__name__)

# db_connection = db.connect_to_database()

# Routes 
@app.route('/')
def root():
    welcome_msg = {
        "message": "Thanks for connecting with my service"
    }

    return json.jsonify(welcome_msg)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    
    app.run(port=port, debug=True) 