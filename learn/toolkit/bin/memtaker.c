
/**
 * 主动占用内存
 */

#include <stdio.h>

#include <stdlib.h>
#include <string.h>

#define NODE_SIZE  (500 * 1024)	// 500 KB

static void* s_arrayp[100] = {};
static int s_size = 0;

static int print_status()
{
	printf ("current malloc = %d, total=%d KB\n", s_size, s_size * 500);
	return 0;
}


static int flush_stdin()
{
	while (1)
	{
		char c = getchar();
		if (c == '\n' || c == EOF)
		{
			break;
		}
	}
}

int main()
{
	while (1)
	{
		printf ("option: t/f\n");
		
		char cOption = '0';
		scanf ("%c", &cOption);
		flush_stdin();

		if (cOption == 't')
		{
			void *p = malloc (NODE_SIZE);
			if (p != NULL)
			{
				memset (p, 0, NODE_SIZE);
				s_arrayp [s_size] = p;
				s_size += 1;
			}
			else 
			{
				printf ("malloc failed\n");
			}
		}
		else if (cOption == 'f')
		{
			if (s_size > 0)
			{
				free (s_arrayp[s_size]);
				s_arrayp[s_size] = NULL;
				s_size -= 1;
			}
			else 
			{
				printf ("node clear\n");
			}
		}
		else 
		{
			continue;
		}

		print_status();
	}
	
	return 0;
}