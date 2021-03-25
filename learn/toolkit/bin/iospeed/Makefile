
CPP=arm-himix100-linux-g++

CFLAGS=-g -Wall
LFLAGS=-lpthread

TARGET=iospeed.out

SRC=$(wildcard *.cpp)
HEAD=$(wildcard *.h)

$(TARGET):$(SRC) $(HEAD)
	$(CPP) $(SRC) $(CFLAGS) $(LFLAGS) -o $@

.PHONY:
	clean

clean:
	rm -rf $(TARGET)