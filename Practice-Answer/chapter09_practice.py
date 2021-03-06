"""
1)    βππ=1π  μ κ³μ°νλ ν¨μ sigma(n) μ μμ±νλΌ. (n μ μ μ)
"""
def sigma(n):
    k = list(range(1, n+1))
    return sum(k)


print(sigma(10))

"""
Slide Type
2) λ€μ λ¬Έμ₯ μν νμ output μ ?
"""
s = ("a", "b", "c")
for i in range(1, len(s) + 1):
    sub = ""
    for j in range(i):
        sub = s[j] + sub
    print(sub)
#%%
"""
3) λ€μ λ¬Έμ₯ μν νμ output μ ?
"""
def sum_part(xlist, n):
    sum = 0
    for x in xlist[n]:
        sum = sum + x
    return sum

ylist = [[1, 2], [3, 4], [5, 6], [7, 8]]
x = sum_part(ylist, 2)
print(x)
#%%
"""
Slide Type
4) μ«μλ‘ νΌλΌλ―Έλ λ§λ€κΈ° : νμ μ«μλ₯Ό μλ ₯μΌλ‘ λ°μμ μ’μ° λμΉ­λλ
νΌλΌλ―Έλννλ‘ μΆλ ₯ νλ€.
"""
def pyramid(n):
    for i in range(n):
        print(" " * (n - i), end="")  #(n-i) κ°μ spaceλ₯Ό μΆλ ₯
        for j in range(1, i + 2):     #1 μμ i+1 κΉμ§μ μ«μλ₯Ό μΆλ ₯
            print(j, end="")
        for j in range(i, 0, -1):     #i μμ 1 κΉμ§ μ­μμΌλ‘ μΆλ ₯
            print(j, end="")
        print()
pyramid(7)
#%%
"""
5) μμμ λ²μμ μ«μλ₯Ό λͺ¨λ κ³±νλ ν¨μλ₯Ό μμ±νλΌ.
    ex) multiply(2,4) ==> 2 * 3 * 4 = 24
"""
def multiply(x, y):
    result = 1
    for i in range(x, y+1):
        result = result * i
    return result

print(multiply(2, 4))

"""
6) μ«μλ‘ μ΄λ£¨μ΄μ§ list μ νκ· μ κ΅¬νλ ν¨μλ₯Ό μμ±νλΌ.
   λ¨, built-in ν¨μλ₯Ό μ΄μ©νμ§ μκ³  for loop μ μ΄μ©νμ¬ μλ‘μ΄ ν¨μ μμ±.
"""
def average(lst):
    sum = 0
    for n in lst:
        sum += n
    return sum / len(lst)

print(average([2,3,4,5,6]))
#%%
"""
7) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] μ for λ¬Έμ μ΄μ©νμ¬,

[1,2,3] , 4
[2,3,4] , 5
[3,4,5] , 6
[4,5,6] , 7
[5,6,7] , 8
[6,7,8] , 9
[7,8,9] , 10 μ μΆλ ₯νλΌ
"""
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(x)-3):
    print(x[i:i+3], ',', x[i+3])
#%%
"""
>>λμ λ¬Έμ 
νΌλ³΄λμΉ μμ΄(Fibonacci Sequence)μ κ³μ°νλ νλ‘κ·Έλ¨λ νμ΄μ¬μΌλ‘ κ°λ¨ν μμ±ν  μ
μλ€.

νΌλ³΄λμΉ μμ΄μ 0 κ³Ό 1 λ‘ μμνκ³  λ€μμ μ«μλ μ΄μ  μ«μ λκ°λ₯Ό λν μ«μλ€λ‘
μ΄λ£¨μ΄ μ§λ€.
0, 1, 1, 2, 3, 5, 8, 13 ......

n κ°μ μ«μλ‘ μ΄λ£¨μ΄μ§ νΌλ³΄λμΉ μμ΄μ μΆλ ₯νλ ν¨μλ₯Ό μμ±νλΌ.
"""
def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return new

lst = []
for i in range(10):
    lst.append(fib(i))

print(lst)
