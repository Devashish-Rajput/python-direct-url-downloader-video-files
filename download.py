import urllib.request
import os
os.chdir("/content/drive/MyDrive/myBot/")
i=1
with open('/content/drive/MyDrive/urls.txt') as f:
    links = [line.rstrip() for line in f]
for q in links:
  x=''
  if i<10:
    x=x+'0'+str(i)
  else:
    x=x+str(i)
  import requests
  r = requests.get(q, allow_redirects=True)
  with open('PokemonS01Ep'+x+'[OpToonsIndia].mp4', 'wb') as f:
      f.write(r.content)
  i=i+1
print('Done')
