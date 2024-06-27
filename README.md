# Summary Accumulator

This is an attempt at a summary accumulator. The idea is to use LLMs to summarize text as they are being processed. 

## Inconsistent behaviour

Interestingly, the summary is not working as well as I thought it would. At least with gpt-4o.

```
$ python accumulator.py            
No new relevant content.
The user wants a todo list application written in python.

$ python accumulator.py
The user wants to code a Scrabble application using Go.

$ python accumulator.py
The user wants to code a Scrabble game and prefers to use the Go programming language.

$ python accumulator.py
The user prefers to code a Scrabble game and wants to use the Go programming language.

$ python accumulator.py
The user wants a Scrabble game coded in Go.

$ python accumulator.py
Current Summary: The user would like a Scrabble game coded in Go.

$ python accumulator.py
No new relevant content
The user wants a todo list application written in python.
```