#include <stdio.h>

int main(void)
{
	int a, b;
    int count;
	int arr[1000001] = {0,};
    
    arr[1] = 1;
    count = 0;
    scanf("%d %d", &a, &b);
    for (i = 2; i <= n; i++)
	{
        for (j = 2; i * j <= n; j++)
            arr[i * j] = 1;
    }
    for (i = m; i <= n; i++)
	{
        if(arr[i] == 0)
            count++;
    }
    printf("%d\n",count);
    return (0);
}
