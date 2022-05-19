#include <stdio.h>

int binsearch(int data[], int key)
{
    int low, high, mid;
 
    low = 0;
    high = 8;
    while (low <= high)
	{
        mid = (low + high) / 2;

        if (key == data[mid])
            return (data[mid]); // return found
        else if (key < data[mid]) // search lower
            high = mid - 1;
        else if (key > data[mid]) //search upper
            low = mid + 1;
    }
    return (-1); //if fail to find
}

int main(void)
{
    int tofind;
	int found;
	int arr[9];
    int i;
	int data;
	
	for(i = 0; i <= 8; i++)
	{
		scanf("%d", &data);
		arr[i] = data;
	}
	scanf("%d", &tofind);
	found = binsearch(arr, tofind);
	printf("%d\n", found);
    return (0);
}
