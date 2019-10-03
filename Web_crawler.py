import requests
from bs4 import BeautifulSoup
import cv2
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
           ,'Cookie':'_ga=GA1.2.1210225416.1550476939; getchu_adalt_flag=getchu.com; _gid=GA1.2.1058704444.1555768196; __utma=191556341.1210225416.1550476939.1556079341.1556079341.1; __utmc=191556341; __utmz=191556341.1556079341.1.1.utmcsr=getchu.com|utmccn=(referral)|utmcmd=referral|utmcct=/blog/; __utmb=191556341.1.10.1556079341; ITEM_HISTORY=1036659%7C1037721%7C1039860%7C1026324%7C1012189%7C1043946%7C1043945%7C1044612%7C1025120%7C1041499%7C933144%7C1043947%7C1037723%7C1037720%7C1036869%7C1036870%7C1039864%7C1039865%7C1003950%7C1036836%7C1044558%7C1023510%7C1047492%7C1044014%7C1047510%7C1047490%7C1036834%7C1028936%7C1026532'}
# folder_path="F:\Anime_Girl/Anime_data/"
folder_path="F:/test/"
index=29339
for i in range( 799529 ,831803):
   web = "http://www.getchu.com/soft.phtml?id="
   web= web+str(i)
   web_sit = requests.get(web,headers=headers)
   test = BeautifulSoup(web_sit.text)
   items = test.find_all('img')
   print("-------------------",i)
   for mom,item in enumerate(items):
     # print(item.get('src'))
     a=item.get('src')
     # print(a[-9:-5])
     if a[-10:-5]=="chara":
      # print("???",item.get('src'))
      web=" http://www.getchu.com/"+item.get('src')
      img_name =folder_path+ str(index + 1) + '.png'
      html = requests.get( web)
      index=index+1
      with open(img_name, 'wb') as file:
         file.write(html.content)
         file.flush()
      file.close()
      print('image%d done' % (index + 1))

# web_sit=requests.get("http://www.getchu.com/soft.phtml?id=1036658",headers=headers)
# test=BeautifulSoup(web_sit.content)
# print(test)


# for  imag in  test.select("img"):
#     print (imag["scr"])

# C:\Users\PC\Pictures\animate_girl
# items = test.find_all('img')
#
#
# for index,item in enumerate(items):
#     # print(item.get('src'))
#     a=item.get('src')
#     print(a)
#     # print(a[-9:-5])
#     if a[-10:-5]=="chara":
#      print(item.get('src'))
#      web=" http://www.getchu.com/"+item.get('src')
#      img_name =folder_path+ str(index + 1) + '.png'
#      html = requests.get( web)
#      with open(img_name, 'wb') as file:
#          file.write(html.content)
#          file.flush()
#      file.close()
#      print('image%d done' % (index + 1))
#------------------- 1026537


