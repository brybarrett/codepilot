# tools/bug_finder.py

import openai

# Call GPT to analyze an error message
def explain_bug(error_text):
    prompt = (
        "You are a helpful programming assistant. "
        "Explain the following error message in simple terms, and suggest a possible fix if known:\n\n"
        f"{error_text}"
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
        explanation = f"⚠️ Error calling GPT: {e}"

    return explanation
