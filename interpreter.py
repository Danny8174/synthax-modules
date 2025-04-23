from synthax_core import wait, set_var, ask_ai

def run_synthax(code):
    output = []
    vars_dict = {}
    for line in code.strip().splitlines():
        if line.startswith("wait"):
            arg = line.split("wait",1)[1].strip()
            output.append(wait(arg))
        elif line.startswith("set"):
            key_val = line.split("set",1)[1].strip().split("=", 1)
            output.append(set_var(vars_dict, key_val[0].strip(), key_val[1].strip()))
        elif line.startswith("askAI"):
            prompt = line.split("askAI",1)[1].strip().strip('"')
            output.append(ask_ai(prompt))
        elif line.startswith("log"):
            message = line.partition("log")[2].strip().strip('"')
            output.append(message)
    return "\n".join(output)