NAME = libft.a

FILES = ft_memset ft_bzero \
		ft_memcpy ft_memccpy \
		ft_memmove ft_memchr \
		ft_memcmp ft_strlen \
		ft_strlcpy ft_strlcat \
		ft_strchr ft_strrchr \
		ft_strnstr ft_strncmp \
		ft_atoi ft_isalpha \
		ft_isdigit ft_isalnum \
		ft_isascii ft_isprint \
		ft_toupper ft_tolower \
		ft_calloc ft_strdup \
		ft_substr ft_strjoin \
		ft_strtrim ft_split \
		ft_itoa ft_strmapi \

SRCS_DIR = ./
SRCS = $(addprefix $(SRCS_DIR), $(addsuffix .c, $(FILES)))

OBJS_DIR = ./
OBJS = $(addprefix $(OBJS_DIR), $(addsuffix .o, $(FILES)))

.c.o: $(SRCS)
	gcc -Wall -Wextra -Werror -c -o $@ $<

$(NAME): $(OBJS)
	ar rcs $@ $^

all: $(NAME)

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: clean all

.PHONY: bonus all clean fclean re