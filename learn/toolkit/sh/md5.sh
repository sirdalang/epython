# find ./ -type f -print0 | xargs -0 md5sum > ./md5.txt

find ./ -type f -print0 | xargs -0 md5sum sort -t ' ' -k 2 | > ./md5.txt

# cat md5.txt | sort -t ' ' -k 2 > md5s.txt

# md5sum -c my.md5