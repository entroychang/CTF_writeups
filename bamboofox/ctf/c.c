#include <stdio.h>
#include <string.h>
#define FLAG_LEN 30

char flag[FLAG_LEN] = {72, 75, 71, 72, 69, 69, 76, 69, 82, 113, 105, 58, 110, 57, 85, 120, 57, 124, 59, 57, 125, 59, 100, 109, 85, 59, 100, 85, 105, 119};

int main() {
	char input[64];

	printf("Please input the flag: ");
	scanf("%64s", input);

	int len = strlen(input);
	if (len != FLAG_LEN) {
		printf("No\n");
		return 0;
	}
	// x ^ 10 == flag[i]
	// x == (x ^ y) ^ y
	for (int i = 0; i < len; i++) {
		if ((input[i] ^ 10) != flag[i]) {
			printf("No\n");
			return 0;
		}
	}

	printf("Ya!\n");

	return 0;
}
