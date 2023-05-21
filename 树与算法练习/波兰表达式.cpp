#include<iostream>
#include<stdio.h>
#include<cstring>
//#include<bits/stdc++.h>
#include<cstdlib>
 
using namespace std;
char s[10];
double f()
{
    scanf("%s",s);
    printf("%s\n",s);
    switch(s[0])
    {
        case '+':return f()+f();
        case '-':return f()-f();
        case '*':return f()*f();
        case '/':return f()/f();
        default:return atof(s);
    }
}
int main()
{
    printf("%f\n",f());
    return 0;
}
