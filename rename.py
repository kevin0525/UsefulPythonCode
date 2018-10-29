import os

path = '/home/kevin/workspace/20181015Excavator/dataset2/20181019/20181019_0'
outpath = '/home/kevin/workspace/20181015Excavator/dataset2/20181019'

if not os.path.exists(outpath):
   os.makedirs(outpath)
PicCount=0
for img in os.listdir(path):
    if img != '.DS_Store':
        name = os.path.splitext(img)
        img_segment = name[0]
        extentName = name[1]
        org_name = os.path.join(path,img)
        changed_name = outpath+"/"+"20181019_"+str(PicCount)+extentName
        os.rename(org_name,changed_name)
        PicCount = PicCount +1
