def describe_to_synthax(description):
    # In real use, connect to OpenAI API
    desc = description.lower()
    if "wait" in desc and "seconds" in desc:
        return "wait 2s"
    elif "log" in desc or "say" in desc:
        return 'log "Hello!"'
    elif "ask" in desc and "ai" in desc:
        return 'askAI "What is the meaning of Synthax?"'
    else:
        return "// Could not parse instruction"