
import nltk
from nltk import ne_chunk,pos_tag,word_tokenize
from nltk.tree import Tree
import re
from nltk.corpus import wordnet
import glob
import os


stats_list = []

def read_input(inputfiles):
    data = []
    files = nltk.flatten(inputfiles)

    for i in range(len(files)):
        input_files = glob.glob(files[i])
        for j in range(len(input_files))
            dat = open(input_files[j]).read()
            data.append(dat)
    return data


def get_stats(redacted_type= 'none', count=0):

    if redacted_type =='redacted_names':
        x = " redacted_names : " + str (count)
        stats_list.append(x)
    elif redacted_type == 'redacted_dates':
        x = "redacted_dates : " + str(count)
        stats_list.append(x)
    elif redacted_type == 'redacted_gender':
        x = "redacted_gender : " + str(count)
        stats_list.append(x)
    elif redacted_type == 'redacted_phone' :
        x = "redacted_phone : " + str(count)
        stats_list.append(x)
    elif redacted_type == 'redacted_concept':
        x= " redacted_concept : " + str(count)
        stats_list.append(x)

    return stats_list

def get_names(data):
    names_list = []
    result = []
    for i in range(len(data)):
        temp_file = data[i]
        words = nltk.word_tokenize(temp_file)
        tagged = nltk.pos_tag(words)
        namedEnt = nltk.ne_chunk(tagged)
        for chunk in namedEnt:
            if type(chunk) == Tree:
                if chunk.label() == "PERSON":
                    names_list.append(' '.join([c[0] for c in chunk]))
        for j in names_list:
            temp_file = temp_file.replace( j, '^'*len(j))
        result.append(temp_file)
        string = "redacted_names"
        get_stats(string,len(names_list))
        names_list.clear()

    return result

def get_gender(data):
    genders=['he','she','him','her','his','hers','male','female','man','woman','men','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    sent=data.split('\n')
    result=''
    count_gender=0
    for i in sent:
        tokens=[]
        tokens=nltk.word_tokenize(i)
        count=0
        for j in tokens:
            if j in genders:
                tok="^"*len(j)                
                result+=tok
                result+=" "
                count_gender+=1
            else:
                result+=j
                result+=' '
            count+=1
      
        result+='\n'
        string = "redacted_gender"
        get_stats(string,count_gender )

        
    return result


def get_dates(data):
    text=data
    dates=[] 
    d_1=re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{2,4}",text)
    
    
    for i in d_1:
        dates.append(i)
    tok=""
    for i in dates:
        tok="^"*len(i)
        text=text.replace(i,tok)
    string = "redacted_dates"
    get_stats(string, len(dates))
    return text    
    

def get_phone(data):
    text=data
    p=[]
    p=re.findall(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',text)
    for i in p:
        tok="^"*len(i)
        text=text.replace(i,tok)
    string = "redacted_phones"
    get_stats(string, len(p))    
    return text


def get_concept(data,concept):
    syn_list =[]
    text=data
    sent=data.split('\n')
    concept_list =[]
    result =[]

    for syn in wordnet.synsets(concept):
        for l in syn.lemmas():
            syn_list.append(l.name())

    for i in sent:
        token=[]
        token = nltk.word_tokenize(i)
        for j in token:
            for synonyms in syn_list:
                if synonyms in j:
                    concept_list.append(j)
        for j in concept_list:
            if j in text:
                text = text.replace(j, '^'*len(j))
        result.append(text)

        string = "redacted_concept"
        get_stats(string, len(concept_list))
        concept_list.clear()
    return result


def final_output(inputfiles,data,outputpath):
    filenames =[]
    files = nltk.flatten(inputfiles)
    for i in range(len(files)):
        input_files = glob.glob(files[i])
        for j in range(len(input_files)):
            if '.txt' in  input_files[j]:
                input_files[j] = input_files[j].replace(".txt", ".redacted.txt")
            if '\\' in input_files[j]:
                input_files[j]= input_files[j].split("\\")
                input_files[j] = input_files[j][1]
            filenames.append(input_files[j])

    for i in range(len(data)):
        for j in range(len(filenames)):
            if i==j:
                file_data =data[i]
                p1 = (os.getcwd())
                p2 = (outputpath+'/'+filenames[j])
                file = open(os.path.join(p1,p2), "w" ,encoding="utf-8")
                file.write(file_data)
                file.close()
    return len(filenames)

def write_stats(stats_list=stats_list):

    path = ('stderr/stderr.txt')
    file = open(path, "w", encoding="utf-8")
    for i in range(len(stats_list)):
        file.write(stats_list[i])
        file.write("\n")
    file.close()
    return stats_list


