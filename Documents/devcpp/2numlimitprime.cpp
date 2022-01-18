#include<stdio.h>
main()
{
	int i,num1,num2,count=0,count2=0,j;
	printf("enter starting number limit\n");
	scanf("%d",&num1);
		printf("enter ending number limit\n");
	scanf("%d",&num2);
	printf("the prime numbers between %d and %d are\n",num1,num2);
	for(i=num1;i<=num2;i++)
	{	count=0;
		for(j=1;j<=i;j++)
		{
			if(i%j==0)
			{
				count++;
			}
		}
		if(count==2)
		{
		printf("\n %d is prime",i);
		count2++;
		}
		
	}
	printf("\nthere are %d prime numbers between %d and %d",count2,num1,num2);
	
}
