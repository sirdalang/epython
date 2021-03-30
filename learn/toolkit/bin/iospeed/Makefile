
# CPP=arm-himix100-linux-g++
CPP=g++

CFLAGS=-g -Wall -Wno-unused-function
CFLGAS+=-std=c++11
LFLAGS=-lpthread
LFLAGS+=-static-libstdc++

TARGET=iospeed.out

SRC=$(wildcard *.cpp)
HEAD=$(wildcard *.h)

$(TARGET):$(SRC) $(HEAD)
	$(CPP) $(SRC) $(CFLAGS) $(LFLAGS) -o $@

.PHONY:
	clean

clean:
	rm -rf $(TARGET)
