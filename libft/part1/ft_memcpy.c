/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:39:01 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:39:17 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*new_dest;
	unsigned char	*new_src;

	if (!dest && !src)
		return (0);
	new_dest = dest;
	new_src = (unsigned char *)src;
	while (n--)
		*new_dest++ = *new_src++;
	return (dest);
}
