import hashlib,os,files,time
def md5(fname):
    try:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except OSError as e:
        answer= fname + "  not found"
        return answer

file1=files.file("/tmp/file1.txt")
file2=files.file("/tmp/file2.txt")
file3=files.file("/tmp/file3.txt")

file1.hash=md5(file1.pathname)
file2.hash=md5(file2.pathname)
file3.hash=md5(file3.pathname)

md5file="/tmp/.md5file"

def file_hash_exist():
    if not os.path.exists(md5file):
         print("it doesn't exist")
         print("creating 1 for you ....")
         time.sleep(2)
         f= open(md5file,"w+")
         f.close()
         add_data_hash()

    else :
        print("it exists ")
        add_data_hash()
def add_data_hash():
    with open(md5file,"w") as file:
        file.write(file1.pathname+":"+file1.hash+"\n")
        file.write(file2.pathname+":"+file2.hash+"\n")
        file.write(file3.pathname+":"+file3.hash+"\n")
    file.close()


file_hash_exist()
