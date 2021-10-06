# Makefile for CLISP module set wildcard

srcdir = /home/src/clisp/clisp-2.49/modules/wildcard
CC = gcc -mno-cygwin
CPPFLAGS = -I/usr/local/include
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LIBDIR = /G//gnu//home//src//clisp//clisp-2.49//build-small//
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit

LN = ln

MAKE = make

SHELL = /bin/sh

GENERATED = wildcard.o wildcard.fas libgnu_wc.a
DISTRIBFILES = link.sh Makefile $(GENERATED) \
	$(srcdir)/README $(srcdir)/wildcard.lisp
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

.PHONY : am--refresh clisp-module clisp-module-distrib clean distclean force

wildcard.c wildcard.fas : $(srcdir)/wildcard.lisp
	$(CLISP) -c $(srcdir)/wildcard.lisp -o ./

wildcard.o : wildcard.c config.h gllib
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) \
		-Igllib -I$(srcdir)/gllib -c wildcard.c

am--refresh :

# wildcard relies on src/gllib, so we must also include files in the build dir
gllib libgnu_wc.a : force
	rm -f libgnu_wc.a
	mkdir -p gllib
	test -f gllib/Makefile || sh config.status gllib/Makefile depfiles
	cd gllib; \
	  $(MAKE) srcdir="$(srcdir)/gllib" \
		ACLOCAL_M4="$(srcdir)/gllib/Makefile.am" \
		CFLAGS="$(CFLAGS) -I$(CLISP_LIBDIR)"; \
	  $(LN) libgnu.a ../libgnu_wc.a

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)

clean : force
	rm -f core *.o *.a *.fas *.lib

distclean : clean

force :

