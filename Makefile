CC=g++
LDFLAGS= -lGL -lGLU -lglut
CPPFLAGS=
CFLAGS= -g -lm -Wall

all: DesktopF

DesktopF: desktop_f.cpp
	$(CC) $(CPPFLAGS) $(CFLAGS) -o $@ $< $(LDFLAGS)

