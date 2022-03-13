CC=gcc
CFLAGS=-Wall -Wextra -Werror -Iincludes
HEADERS=libft.h
SRC = ./*.c
COMP = ${SRC:.c=.o}
NAME = libft.a

all: ${NAME}

${NAME}: ${HEADERS} ${COMP}
	ar rcs ${NAME} ${COMP}

clean:
	rm -f ${COMP}

fclean: clean
	rm -f ${NAME}

re: fclean all
