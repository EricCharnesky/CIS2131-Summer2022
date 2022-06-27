def scramble(sentence, stride):
    result = ""
    for index in range(stride):
        result += sentence[index::stride]
    return result

sentence = "Eric Charnesky went to the store"
for stride in range(len(sentence)):
    print(scramble(sentence, stride))
