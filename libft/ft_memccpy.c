/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:37:04 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:37:26 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memccpy(void *dest, const void *src, int c, size_t n)
{
	unsigned char	*new_dest;
	unsigned char	*new_src;
	size_t			i;

	if (!dest && !src)
		return (0);
	new_dest = (unsigned char *)dest;
	new_src = (unsigned char *)src;
	i = 0;
	while (i < n)
	{
		new_dest[i] = new_src[i];
		if (new_src[i] == (unsigned char)c)
			return (dest + (i + 1));
		i++;
	}
	return (0);
}
