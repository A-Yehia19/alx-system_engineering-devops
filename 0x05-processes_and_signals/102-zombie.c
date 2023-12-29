#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>


/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int i;
	int zombiePID;

	for (i = 0; i < 5; i++)
	{
		zombiePID = fork();
		if (zombiePID > 0)
			printf("Zombie process created, PID: %d\n", zombiePID);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
