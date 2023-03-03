CC = g++
CFLAGS = -std=c++11 -Wall -pedantic   
SOURCES_o = one.cpp 
SOURCES_t = two.cpp 

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET_o = one.exe
	TARGET_t = two.exe
else
	RM = rm
	TARGET_o = one
	TARGET_t = two
endif

all:one two run

one:
	$(CC) $(CFLAGS) -o $(TARGET_o) $(SOURCES_o)
two:
	$(CC) $(CFLAGS) -o $(TARGET_t) $(SOURCES_t)

run: 
	$(TARGET_o)
	$(TARGET_t)
	
clean:
	echo $(OS)
	$(RM) *.exe