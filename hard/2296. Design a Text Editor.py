class Node:

    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class TextEditor:

    def __init__(self):
        self.node = Node("|")

    def addText(self, text: str) -> None:
        nextNode = self.node.next
        for char in text:
            newNode = Node(val=char, prev=self.node, next=None)
            self.node.next = newNode
            self.node = self.node.next
        self.node.next = nextNode
        if nextNode:
            nextNode.prev = self.node

    def deleteText(self, k: int) -> int:
        nextNode = self.node.next
        step = 0
        while self.node.val != "|" and k > 0:
            self.node = self.node.prev
            k -= 1
            step += 1
        self.node.next = nextNode
        if nextNode:
            nextNode.prev = self.node
        return step

    def cursorLeft(self, k: int) -> str:
        text_to_return = ""
        
        while self.node.val != "|" and k > 0:
            self.node = self.node.prev
            k -= 1
        
        current = self.node
        while current.val != "|" and len(text_to_return) < 10:
            text_to_return = current.val + text_to_return
            current = current.prev

        return text_to_return

    def cursorRight(self, k: int) -> str:
        text_to_return = ""
        
        while self.node.next and k > 0:
            self.node = self.node.next
            k -= 1

        current = self.node
        while current.val != "|" and len(text_to_return) < 10:
            text_to_return = current.val + text_to_return
            current = current.prev
            
        return text_to_return


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)