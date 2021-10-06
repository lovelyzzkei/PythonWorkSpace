# Makefile for CLISP module syscalls

srcdir = /home/src/clisp/clisp-2.49/modules/syscalls
CC = gcc -mno-cygwin
# __EXTENSIONS__ is necessary so that the Solaris headers declare confstr().
# _REENTRANT is necessary so that the Solaris headers declare lgamma_r().
CPPFLAGS = -I/usr/local/include -D__EXTENSIONS__ -D_REENTRANT
CFLAGS = -O2
CLISP = /home/src/clisp/clisp-2.49/build-small/clisp -K boot  -E UTF-8 -Epathname 1:1 -Emisc 1:1 -norc -norc -q
CLISP_LIBDIR = /G//gnu//home//src//clisp//clisp-2.49//build-small//
CLISP_LINKKIT = /G//gnu//home//src//clisp//clisp-2.49//build-small//linkkit

LN = ln
LN_S = ln

MAKE = make

SHELL = /bin/sh

GENERATED = calls.o bogomips.o posix.fas libgnu_sc.a preload.lisp
DISTRIBFILES = link.sh Makefile $(GENERATED) \
	$(srcdir)/posix.lisp $(srcdir)/README
distribdir =

# default target: make the module
clisp-module : $(GENERATED)

.PHONY : am--refresh clisp-module clisp-module-distrib clean distclean force

# no $(CPPFLAGS) $(CFLAGS) to avoid all optimizations
bogomips.o : $(srcdir)/bogomips.c
	$(CC) -c $(srcdir)/bogomips.c -o bogomips.o

posix.fas: $(srcdir)/posix.lisp
	$(CLISP) -c $(srcdir)/posix.lisp -o ./

calls.m.c: $(srcdir)/calls.c
	$(CLISP) -C $(CLISP_LINKKIT)/modprep $(srcdir)/calls.c ./

calls.o : calls.m.c config.h gllib
	$(CC) $(CPPFLAGS) $(CFLAGS) -I$(CLISP_LINKKIT) \
		-Igllib -I$(srcdir)/gllib -c calls.m.c -o calls.o

preload.lisp : $(srcdir)/preload.lisp
	$(LN_S) $(srcdir)/preload.lisp .

am--refresh :

# syscalls relies on src/gllib, so we must also include files in the build dir
gllib libgnu_sc.a : force
	rm -f libgnu_sc.a
	mkdir -p gllib
	test -f gllib/Makefile || sh config.status gllib/Makefile depfiles
	cd gllib; \
	  $(MAKE) srcdir="$(srcdir)/gllib" \
		ACLOCAL_M4="$(srcdir)/gllib/Makefile.am" \
		CFLAGS="$(CFLAGS) -I$(CLISP_LIBDIR)"; \
	  $(LN) libgnu.a ../libgnu_sc.a

# Make a module distribution into $(distribdir)
clisp-module-distrib : clisp-module force
	$(LN) $(DISTRIBFILES) $(distribdir)

clean : force
	rm -f core *.o *.a *.m.c *.fas *.lib

distclean : clean

force :

