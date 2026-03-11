from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Store last backend response
last_response = None

@app.route('/')
def home():
    if last_response:
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Backend JSON Response</title>
            <style>
                body { font-family: Arial, sans-serif; }
                pre {
                    background: #f4f4f4;
                    padding: 15px;
                    border: 1px solid #ccc;
                    width: fit-content;
                }
            </style>
        </head>
        <body>
            <h2>Backend JSON Response</h2>
            <pre>{{ response }}</pre>
        </body>
        </html>
        """, response=last_response)
    else:
        return "No data submitted yet"

@app.route('/submit', methods=['POST'])
def submit():
    global last_response

    data = request.get_json()

    last_response = jsonify({
        "message": "Form received successfully",
        "data": {
            "name": data.get("name"),
            "email": data.get("email")
        }
    }).get_data(as_text=True)

    return jsonify({
        "message": "Form received successfully",
        "data": {
            "name": data.get("name"),
            "email": data.get("email")
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
