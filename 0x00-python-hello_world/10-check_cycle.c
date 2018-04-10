#include "lists.h"

/**
* check_cycle - checks if linked list is a cycle
* @list: checked list
*
* Return: 0 if no cycle, 1 if there is a cycle
**/ 

int check_cycle(listint_t *list)
{
	listint_t  *node1;
	listint_t  *node2;

	node1 = list;
	node2 = list;

	while (node1 && node2 && node2->next)
	{
		node1 = node1->next;
		node2 = node2->next->next;
	 

		if (node1 == node2)
			return (1);
	}
	return (0);
}
