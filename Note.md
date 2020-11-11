# My notes


## Description
最近公共祖先 (Lowest Common Ancestor) 指的是给定一棵树T及两个节点 (u,v), 找到一个距离根节点最远的节点x, 且x同时是u和v的祖先, 那么x就是它们的最近公共祖先。

```
     6
   /   \
  4     7
 / \     \
2   5     9
```
例如对上图中的二叉搜索树, 2和7的最近公共祖先是6, 4和5的最近公共祖先是4 (一个点可以是自己的祖先)。 

## Input Format
每个测试样例由3行构成      
第一行是序列的长度n     
第二行是序列的所有n个元素        
第三行是两个节点(u,v)     

## Output Format
对于给定的序列，先按照输入顺序构建二叉搜索树T    
再寻找给定节点的最近公共祖先 x=LCA(T,u,v)     
输出结果是节点x的值        

## Sample Input 1
```
6
6 4 2 7 5 9
2 7
```
## Sample Output 1
```
6
```
## Sample Input 2
```
6
6 4 2 7 5 9
4 5
```
## Sample Output 2
```
4
```
