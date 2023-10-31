def are_you_playing_banjo(name):
    lower = name.lower()
    if lower[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"