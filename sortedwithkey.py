# An array of color names.
colors = ["blue", "lavender", "red", "yellow"]
sorted(colors, key=lambda color: len(color), reverse=True)
sorted(colors, key=len, reverse=True)