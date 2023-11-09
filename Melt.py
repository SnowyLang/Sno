f = open("./flake.smd", "r")
endlines = ["<!DOCTYPE html>","<head>","<meta charset=\"UTF-8\">","<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",]
lines = []
mode = ""
hrefed=""
classed=""
for x in f:
  lines.append(x)
def newLine(l,m,s,led):
  dsus=l.strip("\n")
  dsus = l.rstrip("|")
  sess= s.rstrip("\n")
  if m != "title" and m !="stylesheet" and m != "a" and m!="div" and m!="img" and m!="bgcolor" and m!="insert" and m!="favicon" and m!="script" and m!="button":
    #base algorithimicly    
    # dsus = class or the first sess = the second or content
    if dsus != "" and sess != "":
      endlines.append(f"<{m} class=\"{dsus}\">{sess}</{m}>")
  elif m=="title":
    endlines.append(f"<{m}>{dsus.strip("\n")}</{m}>")
  elif m=="stylesheet":
    endlines.append(f"<link rel=\"stylesheet\" href=\"{dsus.strip("\n")}\"/>")
  elif m=="a":
    if dsus != "" and sess != "":
      endlines.append(f"<a href=\"{led}\" class=\"{dsus.strip("\n")}\">{sess}</a>")
  elif m=="div":
    endlines.append(f"<div class=\"{dsus.strip("\n")}\">")
  elif m=="img":
    endlines.append(f"<img src=\"{sess}\" class=\"{dsus.strip("\n")}\"/>")
  elif m=="insert":
    endlines.append(f"<i class=\"{dsus.strip("\n")}\"></i>")
  elif m=="bgcolor":
    endlines.append("<style>body{background-color:"+dsus.strip("\n")+";}</style>")
  elif m=="favicon":
    endlines.append(f"<link rel=\"icon\" type=\"image/x-icon\" href=\"{dsus.strip("\n")}\">")
  elif m=="button":
    endlines.append(f"<button {led.strip("\n")} class=\"{dsus.strip("\n")}\">{sess.strip("\n")}</button>")
  elif m=="script":
    endlines.append(f"<script src=\"{dsus.strip("\n")}\"></script>")
def breakLine(i):
  dresus = int(i)
  for x in range(dresus):
    endlines.append("<br/>")
def ednaDiv():
  endlines.append("</div>")
def generate():
  dolla = 0
  i=0
  z=0
  contents = False
  slothqyeen = False
  classes = ""
  string = ""
  subi=0
  endhead = 0
  whatheadytype = 0
  reallybreak = 0
  loadData=""
  for line in lines:
    for elem in line:
      if elem == "*" and subi==0:
        print("")
      if elem == "&" and subi==0:
        endhead = 1
      if elem == "$" and subi==0:
        dolla = 1
      if elem == "t" and dolla == 1:
        mode = "title"
        dolla=2
      if elem == "!" and dolla == 1:
        mode = "span"
        dolla=2
      if elem == "`" and dolla == 1:
        mode = "script"
        dolla=2
      if elem == "h" and endhead == 1:
        endhead = 0
        endlines.append("H-END")
      if elem == "a" and dolla == 1:
        mode = "a"
        dolla=2
      if elem == "i" and dolla == 1:
        mode = "insert"
        dolla=2
      if elem == "&" and dolla == 1:
        mode = "bgcolor"
        dolla=2
      if elem == "x" and dolla == 1:
        mode = "button"
        dolla=2
      if elem == "f" and dolla == 1:
        mode = "favicon"
        dolla=2
      if elem == "+" and dolla == 1:
        mode = "img"
        dolla=2
      if elem == "%" and dolla == 1:
        mode = "div"
        dolla=2
      if elem == "^" and dolla == 1:
        mode = ""
        ednaDiv()
      if elem == "b" and dolla == 1:
        reallybreak = 1
      elif elem == "r" and reallybreak ==1:
        reallybreak = 2
      elif reallybreak ==2:
        breakLine(elem)
        reallybreak = 0
      # header crap
      if elem == "#" and dolla == 1:
        mode = "h1"
        dolla=2
        whatheadytype +=1
      elif elem == "#" and whatheadytype == 1:
        mode = "h2"
        dolla=2
        whatheadytype +=1
      elif elem == "#" and whatheadytype == 2:
        mode = "h3"
        dolla=2
        whatheadytype +=1
      # end header crap
      if elem == "=" and dolla == 1:
        mode = "stylesheet"
      if elem == "l" and dolla == 1:
        mode = "load"
        dolla=2
        # For all of the simple ones such as just $= yk 
      if elem=="." and dolla == 2 or elem == "=" and dolla == 1:
        contents = True
        dolla = 3
      elif contents:
        classes+=elem
      if contents and elem == "|":
        contents = False
        slothqyeen = True
      elif slothqyeen:
        string+=elem
      subi +=1
    if mode != "load" and dolla >0:
      newLine(classes,mode,string,loadData)
    elif mode == "load":
      print(f"LOADED DATA INTO STORAGE:{classes}")
      dsus = classes.rstrip("\n")
      loadData = dsus
      mode = ""
    classes=""
    i+=1
    subi=0
    dolla=0
    contents = False
    slothqyeen = False
    string = ""
  for lo in endlines:
    x = open("./flake.html", "a+")
    if lo =="H-END":
      x.write("</head>"+"\n")
    else:
      x.write(lo+"\n")
    z+=1
  print("CONVERSION COMPLETE .smd => .html")
generate()
