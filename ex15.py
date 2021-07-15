from sys import argv

script, filename = argv

txt = open(filename)

print(f"Heres your file {filename}:")
print(txt.read())
txt.close()
