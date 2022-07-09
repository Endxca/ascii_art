from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

string=['a','b','d', 'e', 'g', 'o', 'x', 'p', 'q', '#', '$', '%', '&', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Q', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', 'c', 'f', 'h', 'i', 'm', 'k', 'l', '-', 'n', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z',':', ';', '<', '>', '{', 'm', '}','^', 'n', '`','.',"'",'!', '"', '(', ')',"_","|", '*', '/','~']
print(string)
#font = ImageFont.truetype("arial.ttf", size=24)
font="not"
def getSize(txt):
    testImg = Image.new('RGBA', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    if not font=="not":
      return testDraw.textsize(txt,font=font)
    else:return testDraw.textsize(txt)

real=Image.open(input("File name:\n>"))
pixel=list(real.getdata())
str_text=""
incr=0
print("[*]Generating text...")
total_height=[]
real_height=0
for x in pixel:
  incr+=1
  a=int(((x[0]+x[1]+x[2])/3)/2-34)
  str_text+=string[a]
  if real.size[0]==incr:
    width, height = getSize(str_text)
    total_height.append([real_height,str_text])
    real_height+=int(height/2)+1
    str_text=""
    incr=0

print("[+]size: ",width, real_height)
img = Image.new('RGB', (width+4, real_height), "white")
d = ImageDraw.Draw(img)
real_height=2
for i in total_height:
  if not font=="not":
      d.text((2,i[0]), i[1], fill="black",font=font)
  else:
      d.text((2,i[0]), i[1], fill="black")
print("[*]Saving...")
img.save("output.png")
print("[+]Done")
img.show()
