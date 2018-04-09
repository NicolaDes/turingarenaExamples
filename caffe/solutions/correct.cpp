#include <stdio.h>
#include <assert.h>
#include <algorithm>

int pausa(int N, int A[], int B[])
{
    int ps[2*N];
    for (int i = 0; i < N; i++)
        ps[i] = 2 * A[i] + 1;       //Marco gli inizi pausa come dispari
    for (int i = 0; i < N; i++)
        ps[N + i] = 2 * B[i];       //Marco i fine pausa come pari
    std::sort(ps, ps + 2 * N);      //ordino in modo da notare subito le intersezioni tra intervalli
    for (int i = 0; i < 2 * N; i++)
        ps[i] %= 2;                 //Metto 1 per gli inizi pausa e 0 per i fine pausa
    int dottorandi = 0, caffe = 0;
    for (int i = 0; i < 2 * N; i++)
        if (ps[i])
            caffe += (++dottorandi);         //Se ho 2 uni di fila allora questi si offrono un caffe prima a loro stessi e poi ai successori
        else
            --dottorandi;                    //Altrimenti significa che il numero di dottorandi è diminuito e uno è tornato a lavorare.
    return caffe;
}
