import re


class SimpleTextTokenizer:
    def __init__(self, vocab):
        self.str_to_int = {token:integer for integer,token in enumerate(vocab)}
        # Creates an inverse vocabulary that maps token IDs back to the original text tokens
        self.int_to_str = {i:s for s,i in  self.str_to_int.items()}

    def encode(self, text):
         """
         Processes input text into token IDs
         """
         preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
         preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
         preprocessed = [item if item in self.str_to_int else '<|unk|>' for item in preprocessed]
         ids = [self.str_to_int[s] for s in preprocessed]
         return ids
    
    def decode(self, ids):
        """
        Converts token IDs into text
        """
        text = " ".join([self.int_to_str[i] for i in ids]) 

        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text) #Removes spaces before the specified punctuation
        return text