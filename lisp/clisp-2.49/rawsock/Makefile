# Makefile for CLISP module set rawsock

srcdir = /home/src/clisp/clisp-2.49/modules/rawsock
CC = gcc -mno-cygwin
CPPFLAGS = -I/usr/local/include
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit

LN = ln
LN_S = ln

MAKE = make

SHELL = /bin/sh

GENERATED = sock.fas rawsock.o preload.lisp
DISTRIBFILES = link.sh Makefile $(GENERATED) $(srcdir)/sock.lisp
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

sock.fas: $(srcdir)/sock.lisp
	$(CLISP) -c $(srcdir)/sock.lisp -o ./

rawsock.o : rawsock.m.c config.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) \
		-c rawsock.m.c -o rawsock.o

rawsock.m.c : $(srcdir)/rawsock.c
	$(CLISP) -C $(CLISP_LINKKIT)/modprep $(srcdir)/rawsock.c ./

preload.lisp : $(srcdir)/preload.lisp
	$(LN_S) $(srcdir)/preload.lisp .

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)
	mkdir -p $(distribdir)/demos
	$(LN) $(srcdir)/demos/*.lisp $(srcdir)/demos/README $(distribdir)/demos/

clean : force
	rm -f core *.o *.a *.m.c *.fas *.lib

distclean : clean

force :

