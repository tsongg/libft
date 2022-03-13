CC = gcc
CFLAGS = -Wall -Wextra -Werror
NAME = libft.a

SRCS = 
OBJS =
SRCS_Bonus = 
OBJS_Bonus = 

.c.o: $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS) -o $(<:.c=.o)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

bonus: $(OBJS_B)
	ar rcs $(NAME) $(OBJS_Bonus)

all: $(NAME)

clean:
	rm -f $(OBJS) $(OBJS_Bonus)

fclean: clean
	rm -f $(NAME)

re: clean all

.PHONY: bonus all clean fclean re