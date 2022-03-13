CC = gcc
CFLAGS = -Wall -Wextra -Werror
NAME = libft.a

SRCS = 	ft_memset.c ft_memcpy.c ft_memmove.c ft_memcpy.c ft_memccpy.c ft_memchr.c ft_memcmp.c \
		ft_atoi.c ft_isalnum.c ft_isalpha.c ft_isascii.c ft_isdigit.c ft_isprint.c ft_tolower.c ft_toupper.c \
		ft_bzero.c ft_strlen.c ft_strlcpy.c ft_strlcat.c ft_strchr.c ft_strrchr.c

.c.o: $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS) -o $(OBJS)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

all: $(NAME)

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: clean all

.PHONY: bonus all clean fclean re