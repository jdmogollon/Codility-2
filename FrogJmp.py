
# Count minimal number of jumps from position X to Y.


def solution(X, Y, D):
    diff = Y - X 
    hop  = diff / D
    if (diff%D):  # (Incorrenct) if (diff%D) == True: 
        hop += 1 
    
    return hop
    
