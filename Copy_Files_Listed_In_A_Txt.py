import os
import shutil
txtfile = open('/home/kevin/workspace/20181015Excavator/tempFile/test.txt','r')
imagepath = '/home/kevin/workspace/20181015Excavator/original_dataset/dataset_underUsing/Pos'
targetimagepath = '/home/kevin/workspace/20181015Excavator/original_dataset/dataset_underUsing/test'

count = 0

line = txtfile.readline()
line = line[:-1]
while line:
    line = txtfile.readline()
    line = line[:-1]
    #print(line)

    for imgName in os.listdir(imagepath):
        if imgName != '.DS_Store':
            #name = os.path.splitext(img)
            #print(imgName)
            if line == imgName :
                #print (imgName)
                sourceimageName = imagepath +'/'+ imgName
                targetimageName = targetimagepath +'/' + imgName
                shutil.copy(sourceimageName,  targetimageName)
                count = count +1
print (count)

txtfile.close()
