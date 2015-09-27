import os
import shutil

for f in os.listdir(os.getcwd()):
    if f.endswith('docx'):
        zipName = f.split('.')[0]
        zipFile = shutil.copyfile(f,zipName+'.zip')
