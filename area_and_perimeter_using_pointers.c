#include<stdio.h>
#include<conio.h>
void area(int *,int *,int *,int *);
void main()
{
int l,b,are,peri;
//clrscr();
printf("enter the length and breadth of rectangle");
scanf("%d%d",&l,&b);
area(&l,&b,&are,&peri);
printf("\n Main function: \n Area=%d;Perimeter=%d",are,peri);
getch();
}
void area(int *x,int *y,int *are,int *peri)
{
	*are=(*x)*(*y);
	*peri=(2*(*x)+2*(*y));
	printf("\n In area function: \n Area=%d;Perimeter=%d",*are,*peri);
}

/*
enter the length and breadth of rectangle 
4
5

 In area function: 
 Area=20;Perimeter=18
 Main function: 
 Area=20;Perimeter=18
 */