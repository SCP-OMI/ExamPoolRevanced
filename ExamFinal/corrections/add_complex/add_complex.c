#include <stdio.h>
#include <stdlib.h>

typedef struct complexNumber {
	int real;
	int img;
} complex;

void add_Complex(complex num1, complex num2, complex *num3)
{
	*num3.real = num1.real + num2.real;
	*num3.img = num1.img + num2.img;
}

int main(int ac, char **av)
{
	if (ac != 5){
		printf("\n");
		return 0;
	}
	
	complex a, b, sum;

	a.real = atoi(av[1]);
	a.img = atoi(av[2]);;

	b.real = atoi(av[3]);
	b.img = atoi(av[4]);

	printf("\n a = %d + %di", a.real, a.img);

	printf("\n b = %d + %di", b.real, b.img);

	add_Complex(a, b, &sum);
	printf("\n sum = %d + %di", sum.real, sum.img);

	return 0;
}
