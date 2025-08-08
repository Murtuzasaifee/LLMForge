from src.llmforge.tokenizer.SimpleTokenizer import SimpleTokenizer
from src.llmforge.tokenizer.VocabLoader import vocab_loader

def main():
    test_simple_tokenizer()

def test_simple_tokenizer():
    vocab = vocab_loader()
    tokenizer = SimpleTokenizer(vocab)

    text = """"It's the last he painted, you know," 
            Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    print(ids)
    
    decoded_text = tokenizer.decode(ids)
    print(decoded_text)

if __name__ == "__main__":
    main()
