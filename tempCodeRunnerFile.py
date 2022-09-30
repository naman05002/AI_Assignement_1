if(y==0):
            deq.append(va[1])
            deq.popleft()
            tempvar = deq[0]
            tempbool = True
            for element in deq:
                if(element!=tempvar):
                    tempbool=False
            if(tempbool==True):
                break