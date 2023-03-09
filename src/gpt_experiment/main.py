"""some module"""
import os
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    PretrainedConfig,
)

from gpt_experiment import file_reader

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
# print("do i run here")


# def create_some_shared_utility():
#     """some_shared_utility"""
#     print("ddd")
#     a_d = [1, 2, 3]
#     print(a_d)

#     def utility():
#         return 5

#     return utility


config = PretrainedConfig(max_length=3000, truncation=True)


def summarizer(sentence: str):
    """main function"""
    piper = pipeline(
        task="text2text-generation", model=model, config=config, tokenizer=tokenizer
    )
    return piper(sentence)


if __name__ == "__main__":
    # if i am called in a script, execute me.
    full_file_path = os.path.join(
        file_reader.PROJECT_DIR, file_reader.RELATIVE_BASE_PATH
    )

    print("do i run")
    lines = file_reader.read_file(full_file_path)
    # LINES = " ".join(lines)

    FEED_LINE = "".join(lines[30:50])
            
    summary = summarizer(FEED_LINE)
    print(summary)
