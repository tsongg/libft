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
		ft_striteri ft_putchar_fd \
		ft_putstr_fd ft_putendl_fd \
		ft_putnbr_fd \

FILES_B = 	ft_lstnew ft_lstadd_front \
			ft_lstsize ft_lstsize \


SRCS_DIR = ./
SRCS = $(addprefix $(SRCS_DIR), $(addsuffix .c, $(FILES)))
SRCS_B = $(addprefix $(SRCS_B_DIR), $(addsuffix .c, $(FILES_B)))


OBJS_DIR = ./
OBJS = $(addprefix $(OBJS_DIR), $(addsuffix .o, $(FILES)))
OBJS_B = $(addprefix $(OBJS_B_DIR), $(addsuffix .o, $(FILES_B)))


.c.o: $(SRCS)
	gcc -Wall -Wextra -Werror -c -o $@ $<

$(NAME): $(OBJS)
	ar rcs $(NAME) $^

bonus : $(OBJS_B)
	ar rcs $(NAME) $^


all: $(NAME)

clean:
	rm -f $(OBJS) $(OBJS_B)

fclean: clean
	rm -f $(NAME)

re: clean all

.PHONY: bonus all clean fclean re