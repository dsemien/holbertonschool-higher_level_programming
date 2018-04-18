#include "lists.h"
/**
 * recusion_drome - checks against thr return adress of is_pal
 * @head: pointer to head of the list
 * @copyofhead: copy of head address
 */
int recusion_drome(listint_t **head, listint_t *copyofhead)
{
	if (copyofhead == NULL)
		return (1);
	if (recusion_drome(head, copyofhead->next) && (*head)->n == copyofhead->n)
		*head = (*head)->next;
		return (1);
	return (0);
}

/**
 * is_palindrome - function in C that checks if a singly linked list is a palindrome.
 * @head: double pointer to listint_t
 * 
 * Return: 1 true
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	return (recusion_drome(head, *head));
}

