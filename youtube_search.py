import urllib.request
import re
import sys

query = sys.argv[1].strip("\"").replace(" ","+")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])