/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/20 15:33:04 by tsong             #+#    #+#             */
/*   Updated: 2022/03/20 22:00:17 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_count_wd(const char *str, char c)
{
	size_t	count;
	size_t	flag;
	int		i;

	count = 0;
	flag = 0;
	i = 0;
	while (str[i])
	{
		if (str[i] != c && flag == 0)
		{
			flag = 1;
			count++;
		}
		else if (str[i] == c)
			flag = 0;
		i++;
	}
	return (count);
}

size_t	ft_wd_len(char const *s, char c)
{
	size_t	len;
	int		i;

	len = 0;
	i = 0;
	while (s[i] && s[i] != c)
	{
		len++;
		i++;
	}
	return (len);
}

char	*ft_strndup(const char *s, size_t num)
{
	char	*word;
	char	*temp;
	int		i;

	word = (char *)malloc(sizeof(char) * (num + 1));
	if (!word)
		return (0);
	temp = word;
	i = 0;
	while (num > 0)
	{
		temp[i] = s[i];
		i++;
		num--;
	}
	temp[i] = 0;
	return (word);
}

char	**ft_free_str(char **s, int i)
{
	while (i--)
	{
		free(s[i]);
		s[i] = NULL;
	}
	free(s);
	s = NULL;
	return (0);
}

char	**ft_split(char const *s, char c)
{
	size_t	nb;
	size_t	wd_len;
	size_t	count;
	char	**result;

	if (!s)
		return (0);
	count = ft_count_wd(s, c);
	result = (char **)malloc(sizeof(char *) * (count + 1));
	if (!result)
		return (0);
	nb = 0;
	while (nb < count)
	{
		while (*s && *s == c)
			s++;
		wd_len = ft_wd_len(s, c);
		result[nb] = ft_strndup(s, wd_len);
		if (!result[nb])
			return (ft_free_str(result, nb - 1));
		s += wd_len;
		nb++;
	}
	result[count] = NULL;
	return (result);
}
