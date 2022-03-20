/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tsong <tsong@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/20 17:45:27 by tsong             #+#    #+#             */
/*   Updated: 2022/03/20 19:46:25 by tsong            ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*result;
	t_list	*curr;

	if (!lst || !f || !(result = ft_lstnew(f(lst->content))))
		return (0);
	curr = result;
	lst = lst->next;
	while (lst)
	{
		if (!(curr->next = ft_lstnew(f(lst->content))))
		{
			ft_lstclear(&result, del);
			return (0);
		}
		curr = curr->next;
		lst = lst->next;
	}
	return (result);
}
