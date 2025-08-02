from flask import Flask, render_template, request
import openai
import os

# ─── Setup ──────────────────────────────────────────────────────────────────────
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# ─── Home ───────────────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template("index.html", xp_progress=100)

# ─── Regex Explainer ────────────────────────────────────────────────────────────
@app.route('/regex-explainer', methods=["GET", "POST"])
def regex_explainer():
    explanation = None
    regex = ""

    if request.method == "POST":
        regex = request.form.get("pattern", "")
        prompt = f"Explain this regex in simple English:\n{regex}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a helpful assistant that explains regex."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=300
            )
            explanation = response["choices"][0]["message"]["content"]
        except Exception as e:
            explanation = f"⚠️ Error: {str(e)}"

    return render_template("regex_explainer.html", explanation=explanation, pattern=regex)

# ─── API Tester ─────────────────────────────────────────────────────────────────
@app.route('/api-tester', methods=["GET", "POST"])
def api_tester():
    response_data = None
    return render_template("api_tester.html", response_data=response_data)

# ─── Bug Finder ─────────────────────────────────────────────────────────────────
@app.route('/bug-finder', methods=["GET", "POST"])
def bug_finder():
    explanation = None
    code = ""

    if request.method == "POST":
        code = request.form.get("traceback", "")
        prompt = (
            "You are a helpful programming assistant. "
            "Explain the following Python error message and suggest a possible fix:\n\n"
            f"{code}"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for debugging code."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            explanation = response['choices'][0]['message']['content']
        except Exception as e:
            explanation = f"⚠️ Error calling GPT: {str(e)}"

    return render_template("bug_finder.html", explanation=explanation, code=code)

# ─── Error Explainer ────────────────────────────────────────────────────────────
@app.route('/error-explainer', methods=["GET", "POST"])
def error_explainer():
    explanation = None
    traceback = ""

    if request.method == "POST":
        traceback = request.form.get("traceback", "")
        prompt = f"Explain the following Python traceback in simple terms:\n\n{traceback}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a helpful assistant for explaining Python tracebacks."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            explanation = response["choices"][0]["message"]["content"]
        except Exception as e:
            explanation = f"⚠️ Error: {str(e)}"

    return render_template("error_explainer.html", explanation=explanation, traceback=traceback)

# ─── Share Mode Page ────────────────────────────────────────────────────────────
@app.route('/share')
def share():
    return render_template("share.html")

# ─── Easter Egg 404 Handler ─────────────────────────────────────────────────────
@app.errorhandler(404)
def ninja_dojo_xp(error):
    return render_template("404.html"), 404

# ─── Main ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
