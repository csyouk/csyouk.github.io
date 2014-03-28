'''
def censor(text,word):
    L=text.split()
    if word in L:
    return L
print censor('hello here i am','***')    
'''

def censor(text, word):
    stars = ""
    for i in range(0,len(word)):
        stars = stars.join('*'*len(word))
        if word in text:
            text = text.replace(word, stars)
    return text

print censor('this is test','is')