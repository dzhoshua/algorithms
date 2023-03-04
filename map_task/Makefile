CC = g++
CFLAGS = -std=c++17 -Wall -pedantic

SOURCE_CPP = main.cpp
TARGET_PY = main.py
VIEW = graphics.py

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET_CPP = main.exe
else
	RM = rm
	TARGET_CPP = main
endif

all:
	$(CC) $(CFLAGS) -o $(TARGET_CPP) $(SOURCE_CPP)

clean:
	$(RM) *.exe

run: all
	$(TARGET_CPP)
	python $(TARGET_PY)
	python $(VIEW)