#include "lists.h"

/**
 * print_dlistint - Function that prints all the elemts of a doubly linked list
 * @h: Pointer to the list
 *
 * Martin task
 * Return: Nodes number retured
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	/* If pointer to the list is available*/
	while (h != NULL)
	{
		printf("%d\n", h->n);
		count++;
		h = h->next;
	}
	return (count);
}
