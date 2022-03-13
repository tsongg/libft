/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:39:20 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:39:30 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*new_dest;
	unsigned char	*new_src;
	size_t			m;

	m = n;
	if (dest == src || n == 0)
		return (dest);
	if (dest < src)
	{
		new_dest = (unsigned char *)dest;
		new_src = (unsigned char *)src;
		while (m--)
			*new_dest++ = *new_src++;
	}
	else
	{
		new_dest = (unsigned char *)dest + (n - 1);
		new_src = (unsigned char *)src + (n - 1);
		while (n--)
			*new_dest-- = *new_src--;
	}
	return (dest);
}
