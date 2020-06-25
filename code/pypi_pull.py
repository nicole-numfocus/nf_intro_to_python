import xml.etree.cElementTree as ET
import requests


# Project XML
project_xml = 'https://pypi.org/rss/project/arviz/releases.xml'

# XML Parsing
xml_string = requests.get(project_xml).text
tree = ET.fromstring(xml_string)
item = tree.find("channel").find("item")

date = item.find("pubDate").text
title = item.find("title").text

print(project_xml + " " + title + " " + date)
