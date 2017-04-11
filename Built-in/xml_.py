#  xml
#    xml虽然比json复杂，在web中应用不多，但是仍在很多地方需要用到，所以，有必要了解如何操作xml
#
#      DOM vs SAX
#    操作xml有两种方式：dom和sax
#                   dom： 将所有xml读入内存，解析为树，因此占用内存大，解析慢
#                   sax： 流模式，边读边解析，占用内存小，解析快，缺点就是需要我们自己处理事件

#     正常情况下，有限考虑sax

#     三个事件：
#          start_element事件：读取<a href="/">时
#          char_element事件： 读取python时
#          end_element事件： 读取</a>时

from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attars):
        print('sax:start_element: %s, attrs: %s' %(name, str(attars)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

#   除了解析xml外，如何生成xml呢，99%的情况下需要生成xml结构都是非常简单的，因此，最简单的就是拼接字符串
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# return ''.join(L)