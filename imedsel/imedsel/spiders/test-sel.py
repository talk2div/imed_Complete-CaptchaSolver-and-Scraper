from lxml import html
import pprint
with open('source.html','r',encoding='utf-8') as f:
    tree = html.fromstring(html=f.read())
    for each in tree.xpath("//table[@class='rgMasterTable']/tbody/tr"):
            p = {
                'url':each.xpath('.//td[3]/a/@href'),
                'title':each.xpath('.//td[3]/a/@title')
            }
            pprint.pprint(p)