import  sys
print("Mah-Editor")
print("Exit for '--END'")
source_code = ""
while True:
    line = sys.stdin.readline()
    if line.startswith("--END"):
        break
    source_code += line

f = open("text.txt","w+")
f.write(source_code)
f.close()
