import string

searchfile = open("file.txt", "r")
s = "GRAffiti!!@&, 			sWAAAAAg DURrrrrp^$$#@$#@ ZaCHARy 		**!@#!WiLLiams	"
for line in searchfile:
  words = s.split(" ")
  for word in words:
    xord = word.strip()
    yord = xord.lower()
    zord = yord.translate(yord, None, string.punctuation)
    print(zord)
close()