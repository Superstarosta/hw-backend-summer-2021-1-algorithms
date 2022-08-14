from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text = text.strip()
    max=None
    min=None
    if len(text)>0:
        wordlist = text.split()

        max=wordlist[0]
        min=wordlist[0]

        for word in wordlist:
            if len(word) < len(min):
                min = word
            if len(word) > len(max):
                max = word

    if not min or len(min)==len(max):
        return (None,None)
    else:
        return (min, max)