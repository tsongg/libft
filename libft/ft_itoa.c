/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/20 15:58:08 by tsong             #+#    #+#             */
/*   Updated: 2022/03/20 16:32:28 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	get_len(long long int nbr, int plusminus)
{
	int	len;

	len = 0;
	if (nbr == 0)
		return (1);
	while (nbr > 0)
	{
		nbr /= 10;
		len++;
	}
	if (plusminus == -1)
		len++;
	return (len);
}

char	*ft_itoa(int n)
{
	int				plusminus;
	int				len;
	char			*str;
	long long int	nbr;

	nbr = (long long int)n;
	plusminus = 1;
	if (nbr < 0)
	{
		nbr *= -1;
		plusminus = -1;
	}
	len = get_len(nbr, plusminus);
	str = (char *)malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	str[len--] = '\0';
	while (len >= 0)
	{
		str[len--] = '0' + nbr % 10;
		nbr /= 10;
	}
	if (plusminus == -1)
		str[0] = '-';
	return (str);
}
