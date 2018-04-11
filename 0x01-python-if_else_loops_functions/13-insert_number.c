#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to a linked list
 * @number: number to put into node
 * 
 * Return: address of the new node, or NULL if it failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *stuff;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL || (*head)->n >= node->n)
		{
			node->next = *head;
			*head = node;
		}
	else
	{
		stuff = *head;
		while (stuff->next != NULL && stuff->next->n < node->n)
			{
				stuff = stuff->next;
			}
		node->next = stuff->next;
		stuff->next = node;
	}
	return (*head);
}
