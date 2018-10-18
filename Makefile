CC=gcc
CFLAGS= -std=c99 -Wall -pedantic -lm

TARGET = unitcomp

all: $(TARGET)

$(TARGET): $(TARGET).c
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c


