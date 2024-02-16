n=int(input())
ct=0
if n==1:
    ct=1
while (1<<ct)<n:
    ct+=1
print("2 la puterea", ct, "=", 2**ct)