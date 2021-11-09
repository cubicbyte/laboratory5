class Dictionary:
    words = {}

    def addTranslation(self, lang, word, translation):
        word = word.lower()
        if not lang in self.words:
            self.words[lang] = {}

        if not word in self.words[lang]:
            self.words[lang][word] = []
        
        if not isinstance(translation, list):
            translation = translation.lower()
            self.words[lang][word].append(translation)
            return True

        for i in translation:
            i = i.lower()
            self.words[lang][word].append(i)
    
    def getTranslation(self, lang, word):
        word = word.lower()
        if not lang in self.words:
            print('Ошибка: этого языка нету в базе данных')
            return False

        if not word in self.words[lang]:
            print('Ошибка: этого слова нету в базе данных')
            return None
        
        return self.words[lang][word]

def main():
    dict = Dictionary()
    dict.addTranslation('en', 'Sign', ['Табличка', 'Знак', 'Вывеска'])
    dict.addTranslation('en', 'car', 'Машина')
    dict.addTranslation('ru', 'Замок', ['castle', 'Lock'])

    print('Перевод слова sign:', dict.getTranslation('en', 'sign'))
    print('Перевод слова Замок:', dict.getTranslation('ru', 'Замок'))

if __name__ == '__main__':
    main()