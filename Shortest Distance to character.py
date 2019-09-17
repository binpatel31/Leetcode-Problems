class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        list_S = list(S)
        index = [i for i, x in enumerate(list_S) if x == C]
        #print("index",index)
        mini=-1
        end=0
        ans = []
        for i in range(len(list_S)):
            if mini==-1:
                ans.append(abs(index[end]-i))
                if(ans[-1]==0):
                    mini = end
                    end = end+1
            elif mini==len(index)-1:
                ans.append(abs(index[mini]-i))
            else:
                temp = min(abs(i-index[mini]),abs(index[end]-i))
                ans.append(temp)
                if temp==0:
                    mini=end
                    end+=1
        return ans

                
                
            