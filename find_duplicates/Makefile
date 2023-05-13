SOURCES = main.py
ifeq ($(OS), Windows_NT)
	RM = del
	TARGET = main.exe
else
	RM = rm
	TARGET = main
endif

all:
	-o $(TARGET) $(SOURCES)

clean:
	$(RM) $(TARGET)

run: all
	./$(TARGET)
