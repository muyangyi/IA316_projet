# My notes


## Description
最近公共祖先 (Lowest Common Ancestor) 指的是给定一颗树T及两个节点 (u,v), 找到一个距离根节点最远的节点x, 且x同时是u和v的祖先, 那么x就是它们的最近公共祖先。

```
     6
   /   \
  4     7
 / \     \
2   5     9
```
例如对上图中的二叉搜索树, 4和7的最近公共祖先是6, 4和5的最近公共祖先是4 (一个点可以是自己的祖先)。 

The first line contains number of test case.

Each test contains three lines:

the first line indicates the length of sequence.

the second line contains all members of sequence (unsorted).

the third line indicates the node candidates.

Output
Given the sequence, please first build a BST, and find out the lowest common ancestor of given candidates.

## Input Format
每个测试样例由3行构成
第一行是数组的长度
第二行是所有
第三行是

## Output Format
对于给定的序列，先构建二叉搜索树，再寻找给定节点的最近公共祖先
输出结果是一个整数

## Sample Input 1
```
6
6 4 2 7 5 9
4 7
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
