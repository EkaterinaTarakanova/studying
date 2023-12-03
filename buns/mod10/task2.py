import re
import requests

def get_subheadings(url):
    response = requests.get(url)
    html = response.text
    pattern = r'<h3.*?>(.*?)</h3>'
    subheadings = re.findall(pattern, html)
    return subheadings

url = 'http://www.columbia.edu/~fdc/sample.html'
subheadings = get_subheadings(url)
print(subheadings)
