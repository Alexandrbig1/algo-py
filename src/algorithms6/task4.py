class Comment:
    def __init__(self, text: str, author: str):
        self.text: str = text
        self.author: str = author
        self.replies: list[Comment] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: 'Comment'):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This comment has been deleted."
        self.is_deleted = True

    def display(self, level: int = 0):
        indent = "    " * level
        print(f"{indent}{self.author if not self.is_deleted else ''}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)


root_comment = Comment("What a wonderful book!", "Bodja")
reply1 = Comment("The book is a complete disappointment :(", "Andriy")
reply2 = Comment("What's wonderful about it?", "Marina")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Not a book, just a waste of paper...", "Serhiy")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()