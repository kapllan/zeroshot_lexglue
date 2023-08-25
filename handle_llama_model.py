from torch import cuda, bfloat16
import transformers
from transformers import StoppingCriteria, StoppingCriteriaList
import torch
from tqdm import tqdm
import os
from constants import *

tqdm.pandas()

device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

# set quantization configuration to load large model with less GPU memory
# this requires the `bitsandbytes` library
bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=bfloat16
)


def get_llama_model(model_id: str = None):
    if model_id is None:
        model_id = os.path.join(
            os.path.dirname(__file__), '../llama/llama-2-70b-chat-hf')

    # begin initializing HF items, you need an access token
    model_config = transformers.AutoConfig.from_pretrained(
        model_id,
        # use_auth_token=hf_auth
    )

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        config=model_config,
        quantization_config=bnb_config,
        device_map='auto',
        # use_auth_token=hf_auth
    )

    # enable evaluation mode to allow model inference
    model.eval()

    return model


def get_llama_tokenizer(model_id: str = None):
    if model_id is None:
        model_id = os.path.join(
            os.path.dirname(__file__), '../llama/llama-2-70b-chat-hf')

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_id
    )
    return tokenizer


# define custom stopping criteria object
class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_token_ids):
        self.stop_token_ids = stop_token_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        for stop_ids in self.stop_token_ids:
            if torch.eq(input_ids[0][-len(stop_ids):], stop_ids).all():
                return True
        return False


def get_stopping_criteria(tokenizer):
    stop_list = ['\nHuman:', '\n```\n']

    stop_token_ids = [tokenizer(x)['input_ids'] for x in stop_list]

    stop_token_ids = [torch.LongTensor(x).to(device) for x in stop_token_ids]

    stopping_criteria = StoppingCriteriaList([StopOnTokens(stop_token_ids)])

    return stopping_criteria


def get_llama_pipeline(max_new_tokens: int = MAX_OUTPUT_LENGTH):
    tokenizer = get_llama_tokenizer()
    model = get_llama_model()
    llama_model = transformers.pipeline(
        model=model,
        tokenizer=tokenizer,
        return_full_text=False,  # langchain expects the full text
        task='text-generation',
        # we pass model parameters here too
        stopping_criteria=get_stopping_criteria(tokenizer),  # without this model rambles during chat
        temperature=0.1,  # 'randomness' of outputs, 0.0 is the min and 1.0 the max
        max_new_tokens=max_new_tokens,  # max number of tokens to generate in the output
        repetition_penalty=1.1  # without this output begins repeating
    )

    return llama_model


if __name__ == '__main__':
    llama_pipeline = get_llama_pipeline(1000)
    from datasets import load_dataset

    dataset = ' '.join(load_dataset("joelito/lextreme", "german_argument_mining", split="train")['input'][:100])
    # res = llama_pipeline("Summerize this:\n\n" + dataset)
    res = llama_pipeline("Wrtie a long horror story about a girl who gets to know a man and later she finds out he is a murderer.")
    print(res[0]["generated_text"])

    '''data = list()
    with open('./data/instruction-following-examples/swiss_criticality_prediction_citation_considerations.jsonl',
              "r") as f:
        for line in f:
            entry = js.loads(line)
            data.append(entry)
    df = pd.DataFrame(data)[:10]
    df['predictions'] = df.input_text.progress_apply(lambda x: llama_model(x)[0]["generated_text"])
    df.to_json('test_results.json', lines=True, orient="records", force_ascii=False)'''
