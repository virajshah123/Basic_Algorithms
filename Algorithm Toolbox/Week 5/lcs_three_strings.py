
# def lcs2(a, b):
#     len_a = len(a)
#     len_b = len(b)
#     # initialize lcs
#     lcs = []
#     lcs_string = []
#     for i in range(len_a+1):
#         row1 = [0]*(len_b+1)
#         row2 = [[]]*(len_b+1)
#         lcs.append(row1)
#         lcs_string.append(row2)
#     #print(lcs_string)
    
#     for i in range(1,len_a+1):
#         for j in range(1,len_b+1):
#             #print(lcs_string)
#             up = lcs[i-1][j]
#             left = lcs[i][j-1]
#             diagonal = 0
#             if(a[i-1] == b[j-1]):
#                 diagonal = lcs[i-1][j-1] + 1
#             maximum = max(up, left, diagonal)
#             if up == maximum:
#                 temp = lcs_string[i-1][j].copy()
#                 for element in temp:
#                     lcs_string[i][j].append(element)
#             if left == maximum:
#                 temp = lcs_string[i][j-1].copy()
#                 for element in temp:
#                     lcs_string[i][j].append(element)
#             if diagonal == maximum:
#                 temp = lcs_string[i-1][j-1].copy()
#                 if(len(temp) == 0):
#                     lcs_string[i][j].append([a[i-1]])
#                 for element in temp:
#                     element.append(a[i-1])
#                     lcs_string[i][j].append(element)
#             lcs[i][j] = maximum
#     #print(lcs_string)
#     return lcs_string[-1][-1]

# # def lcs3(a, b, c):
# #     lcs_ab_list = lcs2(a, b)
# #     #print(lcs_ab_list)
# #     maxLen = 0
# #     for lcs_ab in lcs_ab_list:
# #         length = len(lcs2(lcs_ab, c)[0])
# #         if length > maxLen:
# #             maxLen = length
# #     return maxLen

def lcs3(a, b, c):
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    # initialize lcs
    lcs = []
    row = [0]*(len_c+1)
    list1 = []
    for j in range(len_b+1):
        list1.append(row)
    for i in range(len_a+1):
        lcs.append(list1)
        
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            for k in range(1, len_c+1):
                up = lcs[i-1][j][k]
                left = lcs[i][j-1][k]
                behind = lcs[i][j][k-1]
                diagonal = 0
                if(a[i-1] == b[j-1] and b[j-1] == c[k-1]):
                    diagonal = lcs[i-1][j-1][k-1] + 1
                lcs[i][j][k] = max(up, left, diagonal, behind)
                #print(lcs[0][0])
    # print(lcs[0][0])
    print(lcs)
    return lcs[-1][-1][-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    l = int(input())
    c = list(map(int,input().split()))
    print(lcs3(a, b, c))
