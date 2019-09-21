import hashlib,os,files
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
print(file1.hash)
print(file2.hash)
print(file3.hash)
