import wikipedia

# Search for a topic
result = wikipedia.summary("India", sentences=2)
print(result)