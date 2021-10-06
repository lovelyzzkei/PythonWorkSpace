# Makefile for CLISP module set regexp

srcdir = /home/src/clisp/clisp-2.49/modules/regexp
CC = gcc -mno-cygwin
CPPFLAGS = -I/usr/local/include
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LIBDIR = /G//gnu//home//src//clisp//clisp-2.49//build-small//
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit
# cannot compile gnulib/regex with c++
# http://sources.redhat.com/bugzilla/show_bug.cgi?id=5200
NO_CXX = 

LN = ln
LN_S = ln

MAKE = make

SHELL = /bin/sh

GENERATED = regexp.fas regexi.o libgnu_rx.a preload.lisp
DISTRIBFILES = link.sh Makefile $(GENERATED) \
	$(srcdir)/README $(srcdir)/regexp.lisp $(srcdir)/regexp.texinfo
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

.PHONY : all am--refresh clisp-module clisp-module-distrib clean distclean force

regexp.fas: $(srcdir)/regexp.lisp
	$(CLISP) -c $(srcdir)/regexp.lisp -o ./

regexi.o : regexi.m.c config.h gllib
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) \
		-Igllib -I$(srcdir)/gllib -c regexi.m.c -o regexi.o

regexi.m.c : $(srcdir)/regexi.c
	$(CLISP) -C $(CLISP_LINKKIT)/modprep $(srcdir)/regexi.c ./

preload.lisp : $(srcdir)/preload.lisp
	$(LN_S) $(srcdir)/preload.lisp .

am--refresh :

# regexp relies on src/gllib, so we must also include files in the build dir
gllib libgnu_rx.a : force
	rm -f libgnu_rx.a
	mkdir -p gllib
	test -f gllib/Makefile || sh config.status gllib/Makefile depfiles
	cd gllib; \
	  $(MAKE) srcdir="$(srcdir)/gllib" \
		ACLOCAL_M4="$(srcdir)/gllib/Makefile.am" \
		CFLAGS="$(CFLAGS) -I$(CLISP_LIBDIR) $(NO_CXX)"; \
	  $(LN) libgnu.a ../libgnu_rx.a

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)

clean : force
	rm -f core *.o *.a *.m.c *.fas *.lib

distclean : clean

force :

