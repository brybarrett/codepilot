from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regex-explainer', methods=['POST'])
def regex_explainer():
    pattern = request.form['pattern']

    # Simulated GPT-style response (temporary)
    explanation = (
        "This regex matches a U.S. Social Security number format: "
        "three digits, followed by a dash, two digits, another dash, and four digits.\n\n"
        "Example: 123-45-6789"
    )

    return render_template('index.html', pattern=pattern, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)
