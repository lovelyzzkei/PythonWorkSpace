${MAKE-make} clisp-module \
  CC="${CC}" CPPFLAGS="${CPPFLAGS}" CFLAGS="${CFLAGS}" \
  CLISP_LINKKIT="$absolute_linkkitdir" CLISP="${CLISP}"
NEW_FILES="rawsock.o"
NEW_LIBS="${NEW_FILES}  -lws2_32"
NEW_MODULES="rawsock"
TO_LOAD='sock'
TO_PRELOAD='preload.lisp'
