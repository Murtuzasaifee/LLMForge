from pathlib import Path
import re

def vocab_loader():
    # Find the project root by looking for pyproject.toml
    current_path = Path.cwd()
    project_root = current_path
    while not (project_root / "pyproject.toml").exists() and project_root != project_root.parent:
        project_root = project_root.parent

    data_file = project_root / "src" / "llmforge" / "data" / "training" / "the-verdict.txt"

    with open(data_file, "r", encoding="utf-8") as f:
        raw_text = f.read()
        
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    print(preprocessed[:30])

    all_tokens = sorted(list(set(preprocessed)))
    all_tokens.extend(["<|endoftext|>", "<|unk|>"])
    vocab = {token:integer for integer,token in enumerate(all_tokens)}
    
    return vocab