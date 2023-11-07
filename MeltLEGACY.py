f = open("./flake.smd", "r")
endlines = []
lines = []
mode = ""
hrefed=""
classed=""
for x in f:
  lines.append(x)
def header(l):
  mode = "h1"
  # print(lines[l])
  # dsus = lines[l].strip("$#")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$#")
  endlines.append(f"<h1>{store}</h1>")
def breakln():
  endlines.append("<br/>")
def divStart(l):
  mode = "divS"
  # dsus = lines[l].strip("$%")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$%")
  endlines.append(f"<div class=\"{store}\">")
def title(l):
  mode = "divS"
  # dsus = lines[l].strip("$t")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$t")
  endlines.append(f"<title>{store}</title>")
def divEnd(l):
  mode = "divS"
  # dsus = lines[l].strip("$%")
  # lines[l] = dsus
  endlines.append("</div>")
def styles(l):
  mode = "style"
  # dsus = lines[l].strip("$=")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$=")
  endlines.append(f"<link rel=\"stylesheet\" href=\"{store}\"/>")
def textfr(l):
  mode = "text"
  # dsus = lines[l].strip("$!")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$!")
  endlines.append(f"{store}")
def atag(l,hrf):
  mode = "a"
  # dsus = lines[l].strip("$a")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$a")
  endlines.append(f"<a href=\"{hrf}\">{store}</a>")
def span(l,hrf):
  mode = "span"
  # dsus = lines[l].strip("$-")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$-")
  endlines.append(f"<span class=\"{hrf}\">{store}</span>")
def hehepp(l,hrf):
  mode = "p"
  # dsus = lines[l].strip("$p")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$p")
  endlines.append(f"<p class=\"{hrf}\">{store}</p>")
def img(l,hrf):
  mode = "img"
  # dsus = lines[l].strip("$+")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$+")
  endlines.append(f"<img class=\"{hrf}\" src=\"{store}\" alt=\"nobody\"/>")
def bgcolor(l):
  mode = "+"
  # dsus = lines[l].strip("$|")
  # lines[l] = dsus
  endlines.append("<style>body{background-color:"+(lines[l].rstrip("\n")).lstrip("$|")+";}</style>")
def insert(l):
  mode = "i"
  # dsus = lines[l].strip("$i")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$i")
  endlines.append(f"<i class=\"{store}\"></i>")
def favico(l):
  mode = "f"
  # dsus = lines[l].strip("$i")
  # lines[l] = dsus
  store=(lines[l].rstrip("\n")).lstrip("$f")
  endlines.append("<link rel=\"icon\" type=\"image/x-icon\" href=\""+store+"\"/>")
def generate():
  dolla = 0
  bolla = 0
  i=0
  subi=0
  for line in lines:
    for elem in line:
      if elem == "*" and subi == 0:
        print("comment")
      if elem == "$" and subi==0:
        dolla = 1
      if elem == "#" and dolla == 1:
        header(i)
        dolla = 0
      if elem == "b" and dolla == 1:
        breakln()
        dolla = 0
      if elem == "%" and dolla == 1:
        divStart(i)
        dolla = 0
      if elem == "^" and dolla == 1:
        divEnd(i)
        dolla == 0
      if elem == "=" and dolla == 1:
        styles(i)
        dolla = 0
      if elem == "t" and dolla == 1:
        dolla= 0
        title(i)
      if elem == "." and dolla == 1:
        dolla=0
        dsus = lines[i].strip("$.")
        lines[i] = dsus
        hrefed = (lines[i].rstrip("\n")).lstrip("$.")
      if elem == "a" and dolla ==1:
        dolla = 0
        atag(i,hrefed)
      if elem == "-" and dolla ==1:
        dolla = 0
        span(i,classed)
      if elem == "|" and dolla ==1:
        dolla = 0
        bgcolor(i)
      if elem == "i" and dolla ==1:
        dolla = 0
        insert(i)
      if elem == "p" and dolla ==1:
        dolla = 0
        hehepp(i,classed)
      if elem == "l" and dolla == 1:
        dolla=0  
        dsus = lines[i].strip("$l")
        lines[i] = dsus
        classed = (lines[i].rstrip("\n")).lstrip("$l")
      if elem == "!" and dolla == 1:
        textfr(i)
        dolla = 0
      if elem == "+" and dolla == 1:
        dolla = 0
        img(i,classed)
      subi +=1
      if elem == "f" and dolla == 1:
        dolla = 0
        favico(i)
    i+=1
    subi=0
  z = 0
  for lo in endlines:
    if z==1:
        endlines.append("<head>")
        endlines.append("<meta charset=\"UTF-8\">")
        endlines.append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        x = open("./flake.html", "a+")
        x.write(lo+"\n")
        z+=1
        endlines.append("</head>")
    else:
      x = open("./flake.html", "a+")
      x.write(lo+"\n")
      z+=1
      # print(lo)
  print("CONVERSION COMPLETE .smd => .html")
generate()
