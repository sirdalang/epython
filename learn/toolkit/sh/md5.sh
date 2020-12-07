find ./ -type f -print0 | xargs -0 md5sum > ./md5.txt

# md5sum -c my.md5