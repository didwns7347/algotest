nquer=[]
class Node:
    def __init__(self,val,leaf=False):
        self.val= val
        self.leaf=leaf
        self.cnt = 0
        self.child={}
        
class Trie:
    def __init__(self):
        self.head=Node(None)
    def insert(self, word):
        cur=self.head
        for w in word:
            if w not in cur.child:
                cur.child[w]=Node(w)
            cur.cnt+=1
            cur=cur.child[w]
        cur.cnt+=1
        cur.leaf=True
    def search(self,word):
        ret=0
        cur=self.head
        for w in word:
            if w in cur.child:
                cur=cur.child[w]
            else:
                return 0
        node_list=[]
        for c in cur.child:
            node_list.append(cur.child[c])
        for i in node_list:
            ret+=i.cnt
        return ret
            
def solution(words, queries):
    tr = Trie()
    answer=[]
    TR = [ Trie() for _ in range(10000)]
    RTR= [ Trie() for _ in range(10000)]
    for w in words:
        TR[len(w)-1].insert(w)
        RTR[len(w)-1].insert(w[::-1])
    for query in queries:
        flag=False
        if query[0]=="?" and query[-1]!="?":
            flag=True
            query = query[::-1]
        pre=0
        for idx ,c in enumerate(query):
            if c == "?":
                pre = idx
                break
        if flag:
            answer.append(RTR[len(query)-1].search(query[:pre]))
        else:
            answer.append(TR[len(query)-1].search(query[:pre]))
    return answer
w= ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(w,q))
            
    
    
        
