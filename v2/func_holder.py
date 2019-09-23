from __future__ import with_statement
from __future__ import absolute_import
import hashlib,os,files,time,sys
from io import open
def md5(fname):
     if os.path.exists(fname):
        hash_md5 = hashlib.md5()
        with open(fname, u"rb") as f:
            for chunk in iter(lambda: f.read(4096), ""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    else :
        f= open(fname,u"w+")
        f.close()
        return md5(fname)

def file_hash_exist_solve():
    if not os.path.exists(md5file):
         print u"please run script again"
         print u"wait while creating 1 the config file for you ...."
         time.sleep(2)
         f= open(md5file,u"w+")
         f.close()
         add_data_hashfile()

    else :
        compare_data(file1.pathname,file1.hash)
        compare_data(file2.pathname,file2.hash)
        compare_data(file3.pathname,file3.hash)
        add_data_hashfile()

def add_data_hashfile():
    with open(md5file,u"w") as file:
        file.writelines(file1.pathname+u":"+file1.hash+u"\n")
        file.writelines(file2.pathname+u":"+file2.hash+u"\n")
        file.writelines(file3.pathname+u":"+file3.hash+u"\n")
    file.close()

def compare_data(fname,hash):
    with open(md5file,u"r") as file:
        readedfile=file.readlines()
    for element in xrange(len(readedfile)):
        spar=readedfile[element].split(u":")
        if (spar[0] ==fname):
            if (spar[1].rstrip(u"\n")==hash):
                return
            else :
                print fname+u" is  modified"
                return

file1=files.file(u"/tmp/file1.txt")
file2=files.file(u"/tmp/file2.txt")
file3=files.file(u"/tmp/file3.txt")

file1.hash=md5(file1.pathname)
file2.hash=md5(file2.pathname)
file3.hash=md5(file3.pathname)

md5file=u"/tmp/.md5file"

file_hash_exist_solve()
