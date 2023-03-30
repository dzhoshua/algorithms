CC = g++
CFLAGS = -std=c++17 -Wall -pedantic
SOURCES = ndarray.cpp

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET = ndarray.exe
else
	RM = rm
	TARGET = ndarray
endif

all:
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES)

clean:
	$(RM) $(TARGET)

run: all
	$(TARGET)
