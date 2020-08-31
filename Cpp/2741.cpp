#include "stdio.h"

int main() {
    int N;

    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        printf("%d", i+1);
        if(i != N-1) puts("");
    }

    return 0;
}

