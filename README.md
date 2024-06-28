# Summary Accumulator

This is an attempt at a summary accumulator. The idea is to use LLMs to summarize text as they are being processed. 

## Inconsistent behaviour

Interestingly, the summary is not working as well as I thought it would. The first try was fine where both `gpt-4o` and `claude-sonnet-3.5` gave the right updated summary:

```
$ python accumulator.py 
OpenAI: Updated Summary: The user wants to code a Scrabble game and prefers to use the Go programming language.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
OpenAI: Updated Summary: The user wants a Scrabble game coded in Go.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
OpenAI: The user wants a Scrabble game coded in Go.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
OpenAI: Updated Summary: The user wants a Scrabble game coded in Go.
Anthropic: Updated Summary: The user has changed their request. They now want to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
OpenAI: Updated Summary: The user wants to code a Scrabble game using Go.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
```

But another attempt had `gpt-4o` giving the incorrect answer 3/5 times.
```
$ python accumulator.py
OpenAI: Updated Summary: The user wants to code a Scrabble game using Go.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
No new relevant content.
OpenAI: The user wants a todo list application written in python.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
no new relevant content
OpenAI: The user wants a todo list application written in python.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
No new relevant content.
OpenAI: The user wants a todo list application written in python.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
OpenAI: The user wants a Scrabble game coded in Go.
Anthropic: Updated Summary: The user has changed their mind and now wants to code a Scrabble game using the Go programming language instead of a todo list application in Python.
==========
```