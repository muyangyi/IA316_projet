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
例如对上图中的二叉搜索树, 4和7的最近公共祖先是6, 4和5的最近公共祖先是4(一个点可以是自己的祖先)。 

The first line contains number of test case.

Each test contains three lines:

the first line indicates the length of sequence.

the second line contains all members of sequence (unsorted).

the third line indicates the node candidates.

Output
Given the sequence, please first build a BST, and find out the lowest common ancestor of given candidates.

## Input Format
单个字符串s，含有**小写英文字母**、**数字**和**小括号**        
字符串长度 0 <= length(s) <= 1000      
可以确保括号是成对出现的

## Output Format
处理后的字符串结果（正确翻转，不包含数字和小括号）

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
