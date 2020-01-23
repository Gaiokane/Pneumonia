import urllib.request,re
import datetime

def get_html():
    try:
        url='https://3g.dxy.cn/newh5/view/pneumonia'
        request = urllib.request.Request(url)
        request.add_header('User-Agent','Chrome/79.0.3945.130')
        return urllib.request.urlopen(request).read().decode('UTF-8')
    except SystemExit as e:
        print(e)

#print(get_html())

try:
    html=get_html()
    #去空格
    nospace_text = ''.join(html.split())
    #print(nospace_text)
        
    pattern = re.compile('<divclass="descBox___3dfIo">(.*?)</div><divclass="descBox___3dfIo">')
    div_list=re.findall(pattern,nospace_text)
    #print(div_list[0])
    pattern1 = re.compile('<pclass="descList___3iOuI">(.*?)</p>')
    dls=re.findall(pattern1,div_list[0])
    #print(len(dls))
    print(dls)
except SystemExit as e:
    print(e)