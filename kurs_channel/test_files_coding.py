
f = open('123.jpg', 'rb')
res = f.read()
with open('new.jpg','wb') as jpeg_file:
    jpeg_file.write(res)
