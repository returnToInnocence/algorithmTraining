#include <bits/stdc++.h>
using namespace std;

int line[65],len,nxt[65],end,sum;
bool vis[65];
bool cmp(const int a,const int b) {
	return a>b;
}
bool perm(int pre,int fromp) {
	int i;
	if(pre%len==0) {
		if(sum-pre==len) return true;//优化VII
		for(i=2; i<=end && vis[i]; i++) ; //优化V
		vis[i]=true;
		if(perm(pre+line[i],2)) return true;
		vis[i]=false;//后面是else不运行，直接到后面的return false；这就是优化VIII
	} else for(; fromp<=end; fromp++) { //优化VI，直接从继承过来的fromp开始遍历
			if(!vis[fromp]) { //优化IV
				if(pre%len+line[fromp]<=len) {
					vis[fromp]=true;
					if(perm(pre+line[fromp],fromp)) return true;//fromp即为优化VI
					vis[fromp]=false;
					if(pre%len+line[fromp]==len) return false;//优化IX
				}
				fromp=nxt[line[fromp]];//优化II
			}
		}
	return false;
}

int main() {
	int n,iA,in,maxi=0,cha=0,cun=0;
//   n是指木棍根数
	scanf("%d\n",&n);
	for (iA=1; iA<=n; iA++) {
//        in读入每一根木棍
		scanf("%d",&in);
//		如果输入大于50则自动舍去
		if(in<=50) {
//		    找最长的木棍（后面作为选择原木棍可能长度的依据）
			maxi=max(maxi,in);
//			求木棍总和
			sum+=in;
//			对于无法存入的木棍，不让其影响其他木棍相邻存入，因此减去cha
//            line保存所有木棍
			line[iA-cha]=in;
		} else cha++;
	}

//	降序排列，保证先选择大的木棍
	sort(line+1,line+n-cha+1,cmp);//优化I

//	这里的n-cha就是可用的木棍根数
	for(iA=1; iA<=n-cha; iA++)
		if(line[iA]!=cun) {
			nxt[cun]=iA-1;
			cun=line[iA];
		}
	end=n-cha;
	vis[1]=true;
	nxt[line[end]]=end;
	for(len=maxi; len<=sum/2; len++) {
		if(sum%len!=0) continue;//优化III
		if(perm(line[1],2)) break;
	}
	if(len>sum/2) cout<<sum;
	else cout<<len;
	return 0;
}