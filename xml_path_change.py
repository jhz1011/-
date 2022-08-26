import os
import os.path
import xml.dom.minidom
path = r'C:\pythonx\yolo\yolov5-fire\data2\Annotations'
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
count = 0

sv_path=r'C:\pythonx\yolo\yolov5-fire\data2\Annotations' # 修改后的xml文件存放路径
files=os.listdir(path)


for xmlFile in files:
	dom=xml.dom.minidom.parse(os.path.join(path,xmlFile)) #打开xml文件，送到dom解析
	root=dom.documentElement #得到文档元素对象
	item=root.getElementsByTagName('path') #获取path这一node名字及相关属性值
	a,b=os.path.splitext(xmlFile) #分离出文件名a
	for i in item:
         # i.firstChild.data = a + '.
		 i.firstChild.data = 'C:/pythonx/yolo/yolov5-fire/data2/Annotations/'+a+'.jpg'
	with open(os.path.join(sv_path,xmlFile),'w') as fh:
		dom.writexml(fh)





# for xmlFile in files:  # 遍历文件夹
#     if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
#             name1 = xmlFile.split('.')[0]
#             dom = xml.dom.minidom.parse(path + '/' + xmlFile)
#             root = dom.documentElement
#             newfolder = root.getElementsByTagName('folder')
#             newpath = root.getElementsByTagName('path')
#             newfilename = root.getElementsByTagName('filename')
#          #   newfolder[0].firstChild.data = 'VOCdevkit\VOC2012\JPEGImages'
#      #       newpath[0].firstChild.data = 'VOCdevkit\VOC2012\JPEGImages' + '\\' + name1 + '.jpg'
#             newfilename[0].firstChild.data = name1 + '.jpg'
#             print(name1)
# 
#             with open(os.path.join(path, xmlFile), 'w') as fh:
#                 dom.writexml(fh)
#                 print('写入name/pose OK!')
#             count = count + 1
