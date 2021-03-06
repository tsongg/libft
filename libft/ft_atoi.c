/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:29:03 by tsong             #+#    #+#             */
/*   Updated: 2022/03/20 17:42:58 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *str)
{
	long long	nbr;
	long long	sign;
	int			i;

	nbr = 0;
	sign = 1;
	i = 0;
	while ((str[i] && str[i] >= 9 && str[i] <= 13) || str[i] == 32)
		i++;
	if (str[i] == '-')
		sign = -1;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i] && '0' <= str[i] && str[i] <= '9')
	{
		if (sign * nbr > 2147483647)
			return (-1);
		if (sign * nbr < -2147483648)
			return (0);
		nbr = nbr * 10 + str[i] - '0';
		i++;
	}
	return (sign * nbr);
}
