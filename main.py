import hashlib
s='devbridge'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
