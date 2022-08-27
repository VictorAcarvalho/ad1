import string


print("="*100)
print("Bem vindo ao programa verificador de frases")

def main():
    print("Digite as linhas abaixo")
    line=input()
    splitedLine = line.split(" ")
    phrases =[]
    splitedStrings= [] 
    vowels ="AaEeIiOoUu"
    if line =='':
        return print("Nenhuma linha não vazia foi lida!!")
    while line != "":
        phrases.append(line)
        splitedStrings.append(splitedLine)
        line=input()
        splitedLine = line.split(" ")        
    mostAccentueLine=mostAccentue(phrases) 
    mostVowel = vowelsCount(mostAccentueLine , vowels)
    bigWord = biggestWord(splitedStrings)
    print("A linha com mais vogais sem acento: {}".format(mostAccentueLine))
    print("Quantidade de vogais sem acento: {}".format(mostVowel))
    print("A maior palavra digita é :  {}".format(bigWord))
    palindrome(phrases)

def mostAccentue(phrasesList):
    mostAccentuesPhrase = (max(phrasesList, key=str.isascii))

    return mostAccentuesPhrase

def vowelsCount(phrase, vowels):
    phraseVowel = [each for each in phrase if each in vowels]
    return len(phraseVowel)


def biggestWord(lst):
    mergedList = []
    for i in lst:
        for j in i:
            mergedList.append(j)
    resulted = max(mergedList,key=len)
    return resulted

def palindrome(lst):
    palindrome= []
    for i in lst :
        if i == i[::-1] :
            palindrome.append(i)
    return print(palindrome)

    
main()


