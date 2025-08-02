
def simulate_gpt_response(task_type, input_data):
    """
    Simulates GPT-like output for different CodePilot tools.
    """
    if task_type == 'regex_explainer':
        return (
            "This regex matches a U.S. Social Security number format:"
            "three digits, a dash, two digits, another dash, and four digits.\n\n"
            "Example: 123-45-6789"
        )
    
    elif task_type == 'api_summary':
        return f"This endpoint appears to return structured data from: {input_data}"
    
    else:
        return "This is a simulated GPT response placeholder."