import json

def save_script(filename, code):
    with open(filename, 'w') as f:
        f.write(code)
    return f"Saved to {filename}"

def load_script(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "// File not found."

def export_as_json(filename, code):
    data = {'synthax_code': code}
    with open(filename, 'w') as f:
        json.dump(data, f)
    return f"Exported as JSON to {filename}"