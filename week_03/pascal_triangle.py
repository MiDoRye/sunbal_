def pascal_tri(n):
    if n == 1:
        return 1
    else:
        answer = [1]
        for i in range(1, n-1):
            answer.append(pascal_tri(n-1)[i]+pascal_tri(n-1)[i-1])
        answer.append(1)
        return answer


print(pascal_tri(8))


# def pascal_tri(n):
#     if n == 1:
#         return 1
#     else:
#         answer = []
#         for i in range(n):
#             if i == 1 or i == n:
#                 answer.append(1)
#             else:
#                 answer.append(pascal_tri(n-1)[i]+pascal_tri(n-1)[i-1])
#         return answer
