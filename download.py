import urllib.request
import os
with open('urls.txt') as f:
    links = [line.rstrip() for line in f]
os.chdir("Your Path to save your files") ### change to download folder where you want to save files
i=1
for q in links:
  x=''
  if i<10:
    x=x+'0'+str(i)
  else:
    x=x+str(i)
  import requests
  r = requests.get(q, allow_redirects=True)
  with open('Your Tite'+x+'something.extension', 'wb') as f: ####### Change the extension like .mp4, .pdf etc...
      f.write(r.content)
  i=i+1
print('Done')
