from operator import index
from re import search


class WordsFinder():
    def __init__(self,*files_names):
        self.file_names = list(files_names)

    def get_all_words (self):
        all_words = {}
        for files in self.file_names:
            with open (files,encoding='utf-8') as file:
                file = file.read().lower()
                symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for i in symbols:
                    file = file.replace(i, '')
                    words = file.split()
                    all_words[files] = words
            return all_words

    def find(self,word):
        wd = word.lower()
        wd_list = []
        index_words = {}
        for name, words in self.get_all_words().items():
            for i in words:
                wd_list.append(i.lower())
            if wd in wd_list:
                index = wd_list.index(wd) +1 #+1 Потому, что отсчет с 0 
                index_words[name] = index
                return index_words

    def count(self,word):
        words_in_file = {}
        for i,word_ in self.get_all_words().items():
            words_in_file[i] = word_.count(word.lower())
        return words_in_file
if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего


