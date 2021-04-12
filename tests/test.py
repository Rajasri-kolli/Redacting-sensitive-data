
import redactor
import nltk

files =  ['*.txt']


def test_read_input():
    files_data = (redactor.read_input(files))
    assert type(redactor.read_input(files)) == list
    for i in range(len(files_data)):
        temp_file = files_data[i]
        assert (len(temp_file)) > 10
    return 0


def test_redact_names():
    counter = 0
    list = (redactor.read_input(files))
    redacted_list = redactor.get_names(list)
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            if '^' in j:
                counter += 1
    assert counter is not None

def test_get_gender():
    counter =0
    list = (redactor.read_input(files))
    redacted_list = redactor.get_gender(list)
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            if '^' in j:
                counter += 1
    assert counter is not None

def test_get_date():
    counter =0
    list = (redactor.read_input(files))
    redacted_list = redactor.get_date(list)
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            if '^' in j:
                counter += 1
    assert counter is not None


def test_get_concept():
    word ='sharp'
    counter =0
    list = (redactor.read_input(files))
    redacted_list = redactor.get_concept(list,word)
    print((redacted_list))
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            if '^' in j:
                counter += 1
    assert counter is not None


def test_get_stats():
    a = redactor.read_input(files)
    a = redactor.get_names(a)
    a = redactor.get_gender(a)
    a= redactor.get_date(a)
    a= redactor.get_phone(a)
    word = 'sharp'
    redactor.get_concept(a,word)
    stats_list =redactor.stats_list
    assert stats_list is not None



