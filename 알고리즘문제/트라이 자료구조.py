class Node(object):
    def __init__(self,key,conut=0):
        self.key=key
        self.child={}
class Trie(object):
    def __init__(self):
        self.head=Node(None)
    def insert(self,word):
        cur=self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node(ch)
            cur = cur.child[ch]
        cur.child["*"]=True
    def search(self,word):
        cur=self.head
        for ch in word:
            if ch not in cur.child and ch !="?":
                return False
            elif ch not in cur.child and ch="?":
                cur=cur.child["?"]
            elif ch in cur.child:
                cur=cur.child[ch]
        if "*" in cur.child:
            return True
trie=Trie()
trie.insert("fro??")
print(trie.search("froto"))
print(trie.search("frodo"))
