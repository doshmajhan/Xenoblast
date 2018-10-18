CC=gcc
CFLAGS= -std=c99 -Wall -pedantic -lm

all: reciever sender

reciever: reciever.c
	$(CC) $(CFLAGS) -o reciever reciever.c unitcomp.c


sender: sender.c
	$(CC) $(CFLAGS) -o sender sender.c unitcomp.c
