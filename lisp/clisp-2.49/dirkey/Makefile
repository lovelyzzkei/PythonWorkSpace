# Makefile for CLISP module set dirkey

srcdir = /home/src/clisp/clisp-2.49/modules/dirkey
CC = gcc -mno-cygwin
CPPFLAGS = -I/usr/local/include
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit

LN = ln
LN_S = ln

MAKE = make

SHELL = /bin/sh

GENERATED = dirkey.o dirkey1.fas preload.lisp
DISTRIBFILES = link.sh Makefile $(GENERATED) $(srcdir)/dirkey1.lisp
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

dirkey1.fas: $(srcdir)/dirkey1.lisp
	$(CLISP) -c $(srcdir)/dirkey1.lisp -o ./

dirkey.m.c: $(srcdir)/dirkey.c
	$(CLISP) -C $(CLISP_LINKKIT)/modprep $(srcdir)/dirkey.c ./

dirkey.o : dirkey.m.c config.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) -c dirkey.m.c -o dirkey.o

preload.lisp : $(srcdir)/preload.lisp
	$(LN_S) $(srcdir)/preload.lisp .

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)

clean : force
	rm -f core *.o *.a *.m.c *.fas *.lib

distclean : clean

force :

