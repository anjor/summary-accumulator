# Summary Accumulator

This is an attempt at a summary accumulator. The idea is to use LLMs to summarize text as they are being processed. 

The tricky bit is the accumulator is not exactly an accumulator. If an assumption in the current state is updated in the new message, the updated summary should incorporate that. 

## Evals

Initial findings show that `gpt-4o` does not do as well as `claude-sonnet-3.5`.

To evaluate this methodically, I put together a [sample dataset](./sample_data.jsonl) with the help of Claude. The same dataset is also available on [huggingface](https://huggingface.co/datasets/anjor/summary-accumulator-eval).