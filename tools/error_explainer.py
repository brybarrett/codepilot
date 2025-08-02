# tools/error_explainer.py

def explain_error(traceback):
    """
    Simple explanation placeholder for stack traces or error messages.
    Replace with advanced logic later.
    """
    if "NameError" in traceback:
        return "🚫 NameError: You are trying to use a variable that hasn’t been defined yet."
    elif "TypeError" in traceback:
        return "🧩 TypeError: You might be using the wrong data type or operation."
    elif "IndexError" in traceback:
        return "📏 IndexError: You're trying to access an item at a position that doesn’t exist in a list."
    elif "KeyError" in traceback:
        return "🔑 KeyError: You’re trying to access a key in a dictionary that doesn’t exist."
    else:
        return "🧠 Sorry, I couldn’t explain that error yet. Try another message!"
