L1=[1,8,6,4]
L2=[76,4,2,5,7]
diff_L1_L2=list(set(L1)-set(L2))
diff_L2_L1=list(set(L2)-set(L1))
total_diff=diff_L1_L2+diff_L2_L1
print(total_diff)
