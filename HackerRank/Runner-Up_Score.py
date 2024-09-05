"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.
"""
try:
    n = int(input())
    numeros= input().split()
    arr= [int(x) for x in numeros]

    if len(numeros)!=n:
        print('ERROR')
    else:
        winner=max(arr)
        runner_up=min(arr)
        for elem in arr:
            if elem>runner_up and elem!=winner:
                runner_up=elem
        print(runner_up)

except ValueError:
    print('Introduce numeros enteros')
