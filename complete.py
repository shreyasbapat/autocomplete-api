from fast_autocomplete import AutoComplete

from data import Data


def complete_sentence(search_phrase, pretrained_data):
    pretrained_data_dict = {sentence : {} for sentence in pretrained_data}
    print(pretrained_data_dict)
    autocomplete = AutoComplete(words=pretrained_data_dict)
    result = autocomplete.search(word=search_phrase, max_cost=3, size=3)
    final_string_list = [output[0] for output in result]
    print(final_string_list)
    data = Data(final_string_list)
    return data