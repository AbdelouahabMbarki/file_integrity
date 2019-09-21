import hashlib,os,files,time,sys
def md5(fname):
    try:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except OSError as e:
        print(fname + "  not found")
        sys.exit()

def file_hash_exist_solve():
    if not os.path.exists(md5file):
         print("please run script again")
         print("wait while creating 1 the config file for you ....")
         time.sleep(2)
         f= open(md5file,"w+")
         f.close()
         add_data_hashfile()

    else :
        compare_data(file1.pathname,file1.hash)
        compare_data(file2.pathname,file2.hash)
        compare_data(file3.pathname,file3.hash)
        add_data_hashfile()

def add_data_hashfile():
    with open(md5file,"w") as file:
        file.writelines(file1.pathname+":"+file1.hash+"\n")
        file.writelines(file2.pathname+":"+file2.hash+"\n")
        file.writelines(file3.pathname+":"+file3.hash+"\n")
    file.close()

def compare_data(fname,hash):
    with open(md5file,"r") as file:
        readedfile=file.readlines()
    for element in range(len(readedfile)):
        spar=readedfile[element].split(":")
        if (spar[0] ==fname):
            if (spar[1].rstrip("\n")==hash):
                return
            else :
                print(fname+" is  modified")
                return

file1=files.file("/tmp/file1.txt")
file2=files.file("/tmp/file2.txt")
file3=files.file("/tmp/file3.txt")

file1.hash=md5(file1.pathname)
file2.hash=md5(file2.pathname)
file3.hash=md5(file3.pathname)

md5file="/tmp/.md5file"

file_hash_exist_solve()
