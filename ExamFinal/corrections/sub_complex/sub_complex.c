#include <stdio.h>

typedef struct complexNumber {
	int real;
	int img;
} complex;

void sub_Complex(complex num1, complex num2, complex *num3)
{
	*num3.real = num1.real - num2.real;
	*num3.img = num1.img - num2.img;
}

int main(int ac, char **av)
{
	if (ac != 5){
		printf("\n");
		return 0;
	}
	
	complex a, b, sub;

	a.real = atoi(av[1]);
	a.img = atoi(av[2]);;

	b.real = atoi(av[3]);
	b.img = atoi(av[4]);

	printf("\n a = %d + %di", a.real, a.img);

	printf("\n b = %d + %di", b.real, b.img);


	sub_Complex(a, b, sub);
	printf("\n sub = %d + %di", sub.real, sub.img);

	return 0;
}
