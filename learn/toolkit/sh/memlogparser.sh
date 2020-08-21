DSTDIR_NAME='LOG'

FILE_USED=$DSTDIR_NAME/"logused.txt"
FILE_FREE="$DSTDIR_NAME/logfree.txt"
FILE_CACHED="$DSTDIR_NAME/logcached.txt"
FILE_FREECACHED="$DSTDIR_NAME/logfreecached.txt"
FILE_TIME="$DSTDIR_NAME/logtime.txt"

if [ ! -d $DSTDIR_NAME ]; then
        echo "creating dir $DSTDIR_NAME"
        mkdir -p $DSTDIR_NAME
fi

echo "input file: $1"
echo "output file: $FILE_USED $FILE_FREE $FILE_CACHED $FILE_FREE $FILE_FREECACHED"

echo "free" > $FILE_FREE
echo "cached" > $FILE_CACHED
echo "used" > $FILE_USED
echo "free+cached" > $FILE_FREECACHED
echo "time" > $FILE_TIME

echo "parsing..."

VAR_LINE=0
cat "$1" | grep 'Mem:.*used' | while read line
do 
        let "VAR_LINE += 2"
        if((VAR_LINE % 100 == 0));then 
                echo "parsing $VAR_LINE line"
        fi
        v_free=$(echo $line | sed 's/^.*used, \([0-9]*\)K.*/\1/')
        v_cach=$(echo $line | sed 's/^.*buff, \([0-9]*\)K.*/\1/')
        v_freecach=$(expr $v_free + $v_cach)
        echo $v_freecach >> $FILE_FREECACHED
done

cat "$1" | grep 'UTC' | while read line
do
        echo $line >> $FILE_TIME
done

echo "parsing finished"