







import hashlib
string='codespeedy.com'
en=string.encode()
h=hashlib.md5(en)
print("the byte equivalent is :",h.digest())
