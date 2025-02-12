
import re


special_tokens = ["<|endoftext|>", "<|unk|>"]

def process_text(raw_text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    all_words = sorted(set(preprocessed))
    all_words.extend(special_tokens)
    return all_words