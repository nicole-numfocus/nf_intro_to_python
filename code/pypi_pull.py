import xml.etree.cElementTree as ET
import requests


# XML file as found on pypi website
project_xml = 'https://pypi.org/rss/project/arviz/releases.xml'

# Steps needed to parse the XML File

# Find the right item in the XML file
xml_string = requests.get(project_xml).text
tree = ET.fromstring(xml_string)
item = tree.find("channel").find("item")

# Get the right item from xml and pull put the publication date and the title
date = item.find("pubDate").text
version = item.find("title").text

# Print the XML file, version, and date of release
print(project_xml + " " + version + " " + date)
