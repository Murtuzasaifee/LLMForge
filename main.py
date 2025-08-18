from src.llmforge.tokenizer.SimpleTokenizer import SimpleTokenizer
from src.llmforge.tokenizer.VocabLoader import vocab_loader

def main():
    # test_simple_tokenizer()
    # test_tokens_outside_vocab()
    test_tokens_outside_vocab_with_extra_vocab()

def test_simple_tokenizer():
    vocab = vocab_loader()
    tokenizer = SimpleTokenizer(vocab)

    text = """"It's the last he painted, you know," 
            Mrs. Gisburn said with pardonable pride."""
    
    ids = tokenizer.encode(text)
    print(ids)
    
    decoded_text = tokenizer.decode(ids)
    print(decoded_text)


def test_tokens_outside_vocab():
    vocab = vocab_loader()
    tokenizer = SimpleTokenizer(vocab)
    
    text = "Hello, do you like tea. Is this-- a test?"
    
    ids = tokenizer.encode(text)
    print(ids)

def test_tokens_outside_vocab_with_extra_vocab():
    vocab = vocab_loader()
    tokenizer = SimpleTokenizer(vocab)
    
    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."

    text = " <|endoftext|> ".join((text1, text2))
    print(text)

    ids = tokenizer.encode(text)
    print(ids)
    
    decoded_text = tokenizer.decode(ids)
    print(decoded_text)

if __name__ == "__main__":
    main()
