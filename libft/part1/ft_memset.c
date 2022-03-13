/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/13 16:39:41 by tsong             #+#    #+#             */
/*   Updated: 2022/03/13 16:39:46 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memset(void *dest, int c, size_t n)
{
	unsigned char	*new_dest;

	new_dest = dest;
	while (n--)
		*new_dest++ = (unsigned char)c;
	return (dest);
}
