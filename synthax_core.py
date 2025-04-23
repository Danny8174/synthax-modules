import time
import openai

def wait(duration):
    seconds = float(duration.replace('s', ''))
    time.sleep(seconds)
    return f"(waited {seconds}s)"

def set_var(vars_dict, key, value):
    vars_dict[key] = value
    return f"(set {key} = {value})"

def ask_ai(prompt):
    # This would connect to OpenAI in a full deployment
    return f"(AI says: This is a stub for: {prompt})"