
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        paragraph = paragraph.split()

        max_count = 0
        prev = ''

        for i in range(len(paragraph)):
            c = 0

            for j in range(len(paragraph)):
                if paragraph[i] == paragraph[j]:
                    c += 1

            if paragraph[i] not in banned:
                if c > max_count:
                    max_count = c
                    prev = paragraph[i]

        return prev
