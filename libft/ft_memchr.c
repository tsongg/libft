/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:37:35 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:37:46 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memchr(const void *b, int c, size_t n)
{
	while (n--)
	{
		if (*(unsigned char *)b == (unsigned char)c)
			return ((void *)b);
		b++;
	}
	return (0);
}
