/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/20 14:08:36 by tsong             #+#    #+#             */
/*   Updated: 2022/03/21 12:21:01 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*str;

	str = (char *)malloc(sizeof(char) * (len + 1));
	if (!str || s == NULL)
		return (0);
	if ((unsigned int)ft_strlen(s) <= start)
		return (ft_strdup(""));
	ft_strlcpy(str, s + start, len + 1);
	return (str);
}
