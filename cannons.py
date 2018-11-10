def rotate(state, pipe_numbers):
    pipe_numbers=set(pipe_numbers)
    pipeState=[1 if x in pipe_numbers else 0 for x,y in enumerate(state)]
    print(pipeState)
    out=[]
    for i in range(len(state)):
        if len([n for n, m in zip(state, pipeState) if n == m and n!=0])==len(pipe_numbers):
            out.append(i)
            print (out)
        a = state.pop()
        state.insert(0,a)
    return out

#rotate=lambda s,p:[i for i in range(len(s))if all(s[(j-i)%len(s)]for j in p)]

# def rotate(state, pipe_numbers):
#     answer = []
#     for i in range(len(state)):
#         temp = [list(state[-i:]+state[:-i])[x] for x in pipe_numbers]
#         if all(item for item in temp):
#             answer += [i]
#     return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
    assert rotate([1,1,1],[0]) == [0,1,2]