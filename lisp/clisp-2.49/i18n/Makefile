# Makefile for CLISP module set i18n

srcdir = /home/src/clisp/clisp-2.49/modules/i18n
CC = gcc -mno-cygwin
CPPFLAGS = -I/usr/local/include
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit

LN = ln
LN_S = ln

MAKE = make

SHELL = /bin/sh

GENERATED = i18n.fas gettext.o preload.lisp
DISTRIBFILES = link.sh Makefile $(GENERATED) $(srcdir)/i18n.lisp
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

i18n.fas: $(srcdir)/i18n.lisp
	$(CLISP) -c $(srcdir)/i18n.lisp -o ./

gettext.o : gettext.m.c config.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) \
		-c gettext.m.c -o gettext.o

gettext.m.c : $(srcdir)/gettext.c
	$(CLISP) -C $(CLISP_LINKKIT)/modprep $(srcdir)/gettext.c ./

preload.lisp : $(srcdir)/preload.lisp
	$(LN_S) $(srcdir)/preload.lisp .

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)

clean : force
	rm -f core *.o *.a *.m.c *.fas *.lib

distclean : clean

force :

