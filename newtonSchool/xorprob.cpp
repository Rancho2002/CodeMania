#include <bits/stdc++.h>
using namespace std;

int main(){
  long long N,X;
  cin>>N>>X;
  vector<long long > vals;
	for(int i =0;i<N;++i){
		long long x;cin>>x;
		vals.push_back(x);
	}
	int sbit;
			 for(sbit=41;sbit>=0;sbit--){
					 if(((X>>sbit)&1ll)==1){
							 break;
					 }
			 }
			 long req1=0ll;
			 while(sbit>=0){
					 int count=0;
					 for(int i=0;i<N;i++){
							 if(((vals[i]>>sbit)&1ll)==1){
									 count++;
							 }
					 }
					 if(2*count<N){
							 if(req1+(1ll<<sbit)<=X){
									 req1|=(1ll<<sbit);
							 }
					 }
					 sbit--;
			 }
			 long ans1=0ll;
			 for(int i=0;i<N;i++){
					 ans1+=(vals[i]^req1);
					
			 }
			 cout<<ans1;
}