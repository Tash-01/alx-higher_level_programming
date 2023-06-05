#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle and 0 if it doesn't have a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *now = list;
	listint_t *after = list;

	if (!list)
		return (0);

	while (now && after && after->next)
	{
		now = now->next;
		after = after->next->next;
		if (now == after)
			return (1);
	}

	return (0);
}
