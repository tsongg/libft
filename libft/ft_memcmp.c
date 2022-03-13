/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:37:55 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:38:08 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

int	ft_memcmp(const void *b1, const void *b2, size_t n)
{
	unsigned char	*s1;
	unsigned char	*s2;

	if ((b1 == 0 && b2 == 0) || n == 0)
		return (0);
	s1 = (unsigned char *)b1;
	s2 = (unsigned char *)b2;
	while (n--)
	{
		if (*s1 != *s2)
			return (*s1 - *s2);
		s1++;
		s2++;
	}
	return (0);
}
