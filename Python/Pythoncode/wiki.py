import wikipedia

# Search for a topic
result = wikipedia.summary("Python programming language", sentences=2)
print(result)