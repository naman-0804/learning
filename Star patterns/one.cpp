#include<iostream>
using namespace std;
int main(){
    int n=6;
    // for(int i=0;i<n;i++)
    // {
    //     for(int j=n-i;j>=1;j--)
    //     {
    //         cout<<"*";
    //     }
    //     cout<<endl;
    // }
    cout<<endl;
    // for(int i=1;i<=n;i++)
    // {
    //     for(int s=1;s<=n-i;s++)
    //     {
    //         cout<<" ";
    //     }
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<" *";
    //     }
    //     cout<<endl;
    // }

    // for(int i=n;i>=1;i--)
    // {
    //     for(int s=1;s<=n-i;s++)
    //     {
    //         cout<<" ";
    //     }
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<" *";
    //     }
    //     cout<<endl;
    // }
    
    // for(int i=1;i<=n;i++)
    // {
    //     for(int j=1;j<=i;j++){
    //         cout<<j;
    //     }
    //     cout<<endl;
    // }

    // for(int i=1;i<=n;i++)
    // {
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<i;
    //     }
    //     cout<<endl;
    // }
    // for(int i=n;i>=1;i--)
    // {
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<j;
    //     }
    //     cout<<endl;
    // }
    // int num=1;
    // for(int i=1;i<=n;i++)
    // {
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<num<<" ";
    //         num++;
    //     }
    //     cout<<endl;
    // }
    // int num=1;
    // for(int i=1;i<=n;i++)
    // {
    //     for(int j=1;j<=n;j++)
    //     {
    //         cout<<num<<" ";
    //         num++;
    //     }
    //     cout<<endl;
    // }
    // int num=1;
    // for(int i = 1; i <= n; i++) 
    // {
    //     if(i % 2 != 0)
    //     {
    //         // left to right
    //         for(int j = 1; j <= n; j++) 
    //         {
    //             cout << num << " ";
    //             num++;
    //         }
    //         cout<<endl;
    //     } 
    //     else 
    //     {
    //         // right to left
    //         int temp = num + n -1;
    //         for(int j = 1; j <= n; j++) 
    //         {
    //             cout << temp << " ";
    //             temp--;
    //         }
    //         num+=n;
    //         cout<<endl;
    //     }
    // }
    // for(int i =1;i<=n;i++)
    // {
    //     for(int j=1;j<=i;j++)
    //     {
    //         if((i+j)%2==1)
    //         {
    //             cout<<"0";
    //         }
    //         else{
    //             cout<<"1";
    //         }
    //     }
    //     cout<<endl;
    // }

    // for(int i=1;i<=n;i++)
    // {   
    //     int ch=65;
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<(char)ch;
    //         ch++;
    //     }
    //     cout<<endl;
    // }
    // int ch=64;
    // for(int i=1;i<=n;i++)
    // {   
    //     ch++;
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<(char)ch;
    //     }
    //     cout<<endl;
    // }
    // for(int i=1;i<=n;i++)
    // {   
    //     int ch=65;
    //     for(int j=n-i-1;j>=1;j--)
    //     {
    //         cout<<(char)ch;
    //         ch++;
    //     }
    //     cout<<endl;
    // }
    // for(int i=1;i<=n;i++)
    // {   
    //     int ch = 65 + i - 1; 
    //     for(int j=1;j<=i;j++)
    //     {
    //         cout<<(char)ch;
    //         ch++;
    //     }
    //     cout<<endl;
    // }
    for(int i = 1; i <= n; i++) {
        // left stars
        for(int j = 1; j <= n - i + 1; j++) {
            cout << "* ";
        }

        // middle spaces
        for(int s = 1; s <= 2*(i-1)+1;s++) {
            cout << "  ";
        }

        // right stars
        for(int j = 1; j <= n - i + 1; j++) {
            cout << "* ";
        }

        cout << endl;
    }

    // Lower half
    for(int i = 1; i <= n; i++) {
        // left stars
        for(int j = 1; j <= i; j++) {
            cout << "* ";
        }

        // middle spaces
        for(int s = 1; s <= 2*(n-i) + 1; s++) {
            cout << "  ";
        }

        // right stars
        for(int j = 1; j <= i; j++) {
            cout << "* ";
        }

        cout << endl;
    }
    return 0;
}