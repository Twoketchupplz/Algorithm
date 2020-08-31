#include "stdio.h"

int main() {
    int count;

    scanf("%d", &count);

    for(int i = 1; i < count+1; i++){
        for(int j = 0; j < count-i; j++) printf(" ");
        for(int j = 0; j < i; j++) printf("*");
        puts("");
    }

    return 0;
}