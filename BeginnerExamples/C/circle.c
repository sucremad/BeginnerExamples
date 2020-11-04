#include <stdio.h>

int main()
{
	int choice;
	float result,radius;

	float pi = 3.14;

	printf("Enter the radius:\n");
	scanf_s("%f", &radius);
	printf("Type 1 for the area,or 0 for the perimeter:\n");
	scanf_s("%d", &choice);

	if (choice == 1)
	{
		result = pi * radius*radius;
		printf("Area of the circle: %.2f\n", result);
	}

	else if (choice == 0)
	{
		result = 2 * pi*radius;
		printf("%.2f", result);
	}
	else
		printf("Invalid Choice!");

	system("pause");

	return 0;

}
