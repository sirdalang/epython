from urllib.request import urlopen

with urlopen('http://www.baidu.com') as response:
    for line in response:
        line = line.decode('utf-8')
        print (line)

file = open ('test.html', 'w')

with urlopen('http://www.baidu.com') as response:
    file.write(response.read().decode('utf-8'))

file.close()