
import heapq
from collections import Counter

def huffman(text):
    freq = Counter(text)

    heap = []
    for ch, f in freq.items():
        heap.append([f, [ch, ""]])

    heapq.heapify(heap)

    if len(heap) == 1:
        return {heap[0][1][0]: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]
        for item in right[1:]:
            item[1] = "1" + item[1]

        new_frequency = left[0] + right[0]
        new_group = left[1:] + right[1:]

        heapq.heappush(heap, [new_frequency] + new_group)

    codes = {}

    for ch, code in heap[0][1:]:
        codes[ch] = code

    return codes

text = input("Enter the String:")
codes = huffman(text)

print("Huffmans Codes:")
for ch, code in codes.items():
    print(repr(ch), ":", code)

encoding = ""

for ch in text:
    encoding = encoding + codes[ch]

print("Haffman Encoded String: ", encoding)
