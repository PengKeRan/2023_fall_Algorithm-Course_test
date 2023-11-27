w = input().split(' ')
n = int(w[0])
query_n = int(w[1])
arr = input().split(' ')
arr = [int(arr[i]) for i in range(n)]
query = input().split()
query = [int(query[i]) for i in range(query_n)]

newarr = []
res = []
hashmap = {}
for i in range(n):
    if arr[i] % 3 != 0:
        newarr.append(arr[i])
        continue
    if arr[i] in hashmap:
        temp = arr[i] // pow(3, hashmap[arr[i]])
        for k in range(pow(3, j)):
            newarr.append(temp)
        continue
    j = 2
    while True:
        if arr[i] % pow(3, j) == 0:
            j += 1
        else:
            j -= 1
            hashmap[arr[i]] = j
            temp = arr[i] // pow(3, j)
            for k in range(pow(3, j)):
                newarr.append(temp)
            break
for i in range(query_n):
    print(newarr[i], end=' ')

# #include <bits/stdc++.h>
# #define MAXN 200005
# using namespace std;
#
# int n,q,l=1,a[MAXN];
# long long s,b[MAXN];
#
# int main()
# {
# 	scanf("%d %d",&n,&q);
# 	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
# 	for (int i=1;i<=q;i++) scanf("%lld",&b[i]);
# 	for (int i=1;i<=n;i++)
# 	{
# 		int c=1;
# 		for (;!(a[i]%3);a[i]/=3) c*=3;
# 		for (s+=c;l<=q&&b[l]<=s;l++) printf("%d%c",a[i]," \n"[l==q]);
# 	}
# 	return 0;
# }