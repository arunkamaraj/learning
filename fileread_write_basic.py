wf = open("arun.txt", "wb", buffering=2 )
wf.write("hi this is first file writing")
wf.close()

rf = open("arun.txt", "rb",-1)
readed = rf.read(5)
print readed

