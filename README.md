
**RAJASRI KOLLI**


In this Project all the sensitive information from the text files  are redacted based on given input flags and commands.



*Info to be redacted*: The redacted flags generally are names, genders, dates, concept and phones.

For the names : nltk and nltk.ne_chunk() are used to identify named entities with labels named "PERSON".


For the dates : the regular expression for identifies the terms/dates of format 'dd/mm/yyyy'

For the Phones : regular expressions are used to identify them finding the following formats of phone numbers such as 'ddd./-ddd./-dddd'

For the genders :  a list of possible genders include =['he','she','him','her','his','hers','male','female','man','woman','men','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']

if  taken any file which has any of the above gender form , it replaces the word.

For the concept : this function identifies synonyms of given concept word with the help of importing wordnet from nltk.corpus

-- All the sensitive information is replaced with ' ^ ' times the length of item to be redacted.


OUTPUT  all the redacted files will go into a separate folder with extensinon redacted .txt 

pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
                    
                    
      If we run the above code in the command line argument , the glob operator identifies multiple input text files and redact all the necessary input flags given and ouput is sent into other new folder. 
      
      stats is the function which when called gives you a brief analysis of the process, here suppose it gives you the count of number of words redacted in each function.


