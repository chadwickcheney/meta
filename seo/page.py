from . import spider
from . import user
import pprint
from . import spider
from . import user
import pprint

class Page:
    def __init__(self,url):
        self.url = url
        self.browser = spider.Browser(url)
        self.dictionary={}
        self.head = self.browser.html.find('head')
        self.dictionary.update(self.elements_to_dictionary(self.head))
        pprint.pprint(self.dictionary)

    def elements_to_dictionary(self, head_elment):
        dictionary={}
        for e in head_elment:
            if 'bs4.element.Tag' in str(type(e)):
                user.prompt(feed="element_name: "+str(e.name), custom=True, custom_space=15)
                key = e.name
                sub_dictionary = {}
                if len(e.attrs) > 1:
                    for attribute in e.attrs:
                        user.prompt(feed="element_attribute: "+str(e[attribute]), custom=True, custom_space=30)
                        sub_key = attribute
                        sub_dictionary.update(self.safe_store(sub_key, e[attribute], sub_dictionary))
                else:
                    key = e.name
                    value = e.getText()
                    dictionary.update(self.safe_store(key, value, dictionary))
                if sub_dictionary:
                    dictionary.update(self.safe_store(key, sub_dictionary, dictionary))
        return dictionary

    def find_tag(self, e, array):
        for a in array:
            user.prompt(feed="looking for "+str(a),custom=True,custom_space=15)
            try:
                var = e[str(a)]
                user.prompt(feed='found '+str(a)+ ": "+str(var),custom=True,custom_space=30)
                return var
            except Exception as error:
                user.prompt(feed="error: "+str(error),custom=True,custom_space=45)
        return False

    def safe_store(self, key, value, dictionary):
        '''#1 key = title, value = Engine 0
        #2 key = title, value = Engine 1 = > key = title, value = {1: Engine 0, 2:Engine 1}
        if multi:
            if not key in dictionary.keys():
                dictionary.update({key:value})
            else:
                print(str(key)+"<=key | value=>"+str(value))
                index = len(dictionary[key].keys())
                index_dictionary={}
                index_dictionary.update({index:value})
                dictionary[key].update({index:value})
        else:'''
        if not key in dictionary.keys():
            dictionary.update({key:value})
        else:
            var = dictionary[key]
            if not 'dict' in str(type(var)):
                dictionary.pop(key)
                index_dictionary={0:var}
                index_dictionary.update({1:value})
                dictionary.update({key:index_dictionary})
            else:
                index = len(var.keys())
                index_dictionary = var
                index_dictionary.update({index+1:value})
                dictionary.update({key:index_dictionary})
        return dictionary
