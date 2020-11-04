#include <stdio.h>

int main()
{
	int secim;
	float sonuc,yaricap;

	float pi = 3.14;

	printf("yaricap degeri giriniz:\n");
	scanf_s("%f", &yaricap);
	printf("alan icin 1,cevre icin 0 degerini giriniz:\n");
	scanf_s("%d", &secim);

	if (secim == 1)
	{
		sonuc = pi * yaricap*yaricap;
		printf("Dairenin alani: %.2f\n", sonuc);
	}

	else if (secim == 0)
	{
		sonuc = 2 * pi*yaricap;
		printf("%.2f", sonuc);
	}
	else
		printf("hatali giris!");

	system("pause");

	return 0;

}
