/*Bisection operation to find root of transcendental equation
  Name: Sagar Dam;  Dept:  DNAP*/

//importing library functions and defining f(x)
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
float function(float x);

//defining main program
void main()
{
	printf("\n #$#$#$#$#   SAGAR'S BISECTION CALCULATOR   #$#$#$#$#  :)\n\n");
   //defining variables
  	int i=0,j=0,n;
   float y=0, x=0, z=0,c;
   float g[25];

   //showing some functional value for user
   for(i=-10; i<=10; i++)
   	{
          g[i]= function(i);
          printf(" The value of f(x) for x=%d is given by:   %f\n",i,g[i]);
      }

   //taking seed values from user
   printf("\n Choose your seed points from the result: \n");
   printf(" first seed point:  ");
   scanf("%f",&x);
   printf("\n second seed point:  ");
   scanf("%f",&y);

   //doing bisection operation...
   if(function(x)>0&&function(y)>0 || function(x)<0 && function(y)<0)
   	{
      	printf("\n these are not seed points");
      }
   else if(function(x)==0)
      {
      	printf("\n the exact solution is: %f",x);
      }
   else if(function(y)==0)
      {
      	printf("\n the exact solution is: %f",y);  
      }
   else if(function(x)>0&&function(y)<0 || function(x)<0 && function(y)>0)
   	{
      	printf("\n\n These are exact seed points....  :)");
         printf("\n Give the no of bisection you want: ");
         scanf("%d",&n);
         if(x>y)
         {
         c=x-y;
         }
         else
         {
         c=y-x;
         }

         printf("\n etn no\t\tx\t\ty\t\tz\t\tf(x)\t\tf(y)\t\tf(z)\n");
         for(i=1; i<=n; i++)
         {
            c=c/2;
         	z=(x+y)/2;
            printf("\n %d\t\t%f\t%f\t%f\t%f\t%f\t%f",i,x,y,z,function(x),function(y),function(z));
            if(function(x)>0&&function(z)>0 || function(x)<0 && function(z)<0)
            {
               x=z;
            }
            else if(function(y)>0&&function(z)>0 || function(y)<0 && function(z)<0)
            {
               y=z;
            }
            else if(function(z)==0)
            {
               printf("\n the result is:  %f",z);
               break;
            }
         }

         printf("\n\n THE BEST NUMERICAL SOLUTION IS FOR x=%f WITH f(x)=%f",z,function(z));
         printf("\n\n With the interval range of:  %f",c);
      }
	getch();
}


//defining the function f(x)=0
float function(float x)
{
	float operation;
   operation= x*x-exp(-x*x);
   return (operation);
}
