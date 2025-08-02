# tools/regex_explainer.py

def explain_regex(pattern):
    """
    Returns a basic explanation for a regex pattern.
    This function can be expanded to use a real LLM/GPT engine.
    """
    if pattern == r"\d{3}-\d{2}-\d{4}":
        return (
            "This regex matches a U.S. Social Security Number (SSN):\n"
            "- \\d{3} matches exactly 3 digits\n"
            "- A hyphen\n"
            "- \\d{2} matches exactly 2 digits\n"
            "- A hyphen\n"
            "- \\d{4} matches exactly 4 digits\n\n"
            "Example: 123-45-6789"
        )
    else:
        return (
            "This is a placeholder explanation.\n\n"
            f"Pattern received: {pattern}\n"
            "Regex parsing not yet implemented for general patterns."
        )
