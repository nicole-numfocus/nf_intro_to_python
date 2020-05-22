import xml.etree.cElementTree as ET
import requests


xml_string = requests.get('https://pypi.org/rss/project/arviz/releases.xml').text
tree = ET.fromstring(xml_string)
tree.find("channel").find("item").find("title").text 
