import sys
import os
import re
import requests as r
import wget

filedir = os.path.join('/home/groot/Downloads')

# Download Low Resolution Video
sd_url = ''
try:
    LINK = input("Enter a Facebook Video Post URL: ")
    html = r.get(LINK)
    sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
    sd_url = sdvideo_url.replace('sd_src:"', '')
except r.ConnectionError as e:
    print("OOPS!! Connection Error.")
except r.Timeout as e:
    print("OOPS!! Timeout Error")
except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")
except (KeyboardInterrupt, SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
except TypeError:
    print("Video May Private or Invalid URL")

if sd_url:
    print("\n")
    print("Normal Quality: " + sd_url)
    print("[+] Video Started Downloading")
    wget.download(sd_url, filedir)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")
