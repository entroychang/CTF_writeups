#include<stdio.h>
#include<sys/mman.h>
int main(){
	char shellcode[0x1000];
	//mprotect(shellcode,0x1000,PROT_READ|PROT_WRITE|PROT_EXEC);
	read(0,shellcode,0x1000);
	char data;
	FILE *fp = fopen("/dev/urandom", "r");
	fread(&data, 1, 1, fp);
	fclose(fp);
	int off = data;
	__asm__("jmp %0"::"r"(shellcode+(unsigned int)off));
	return 0;
}
	