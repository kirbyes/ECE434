TOOLS_CFLAGS	:= -Wstrict-prototypes -Wshadow -Wpointer-arith -Wcast-qual \
		   -Wcast-align -Wwrite-strings -Wnested-externs -Winline \
		   -W -Wundef -Wmissing-prototypes
#
# Programs
#
all:	togglegpio togglegpiolseek

togglegpio:	togglegpio.c gpio-utils.c gpio-utils.h
	$(CC) $(LDFLAGS) -o $@ $^

togglegpiolseek:	togglegpiolseek.c gpio-utils.c gpio-utils.h
	$(CC) $(LDFLAGS) -o $@ $^

#
# Objects
#

%.o: %.c
	$(CC) $(CFLAGS) $(TOOLS_CFLAGS) -c $< -o $@

clean:
	rm gpio-int-test.o gpio-utils.o togglegpio.o gpio-int-test togglegpio
