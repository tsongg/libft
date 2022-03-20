/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/20 17:45:27 by tsong             #+#    #+#             */
/*   Updated: 2022/03/20 21:33:11 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*result;
	t_list	*temp_result;

	if (!lst || !f)
		return (0);
	result = ft_lstnew(f(lst->content));
	if (!result)
		return (0);
	temp_result = result;
	lst = lst->next;
	while (lst)
	{
		temp_result->next = ft_lstnew(f(lst->content));
		if (!temp_result->next)
		{
			ft_lstclear(&result, del);
			return (0);
		}
		temp_result = temp_result->next;
		lst = lst->next;
	}
	return (result);
}
