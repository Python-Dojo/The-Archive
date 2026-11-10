# Task

Create a bot that posts random project ideas into a Discord channel, with the aim of generating discussion, inspiration, or a ridiculous challenge list for the group.

This folder contains two separate approaches from the 2024-11-27 Bristol Python Dojo session. The shared goal is to automate a simple message generator and push it to Discord, where it can appear as a bot posting random prompts or ideas into a chat.

## What the program does

### Group 1: Discord webhook idea bot

The script in `Group-1/main.py` posts a generated suggestion to a Discord webhook.

It does several things:

- picks a random Wikipedia article
- converts the article title into a human-readable phrase
- chooses a random piece of boilerplate language like:
  - "I, the Almighty Ruler, command you to build"
  - "The Mission, should you choose to accept it, is to build"
- creates a full sentence such as:
  - `The hostages will only be freed on the condition that you build a maze builder`
- posts it to a Discord webhook using `requests.post(...)`

The key payload is built here:

```python
def create_body(message: str):
    return {"username": BOT_NAME, "content": message, "avatar_url": random.choice(AVATAR_IMAGES)}
```

Then it sends the payload to `FULL_WEBHOOK_URL`:

```python
response = requests.post(FULL_WEBHOOK_URL, create_body(message))
```

This means the program's output is not just text in the terminal; it is a message posted directly to a live Discord channel.

### Group 2: Discord bot client

The script in `Group-2/main.py` is a more classic bot implementation using the `discord` library.

It creates a bot client and listens for events such as:

- `on_ready()`
- `on_member_join()`
- `on_message()`

When the bot starts, it joins the configured channel and announces itself. It also responds to the keyword `test` by sending a message back into the same chat.

This version is more general-purpose and closer to a reusable bot framework, whereas Group 1 is a one-off idea poster.

## Main concept

The main concept behind both solutions is a bot-driven content generator.

The idea is to make the system produce random prompts or challenge ideas automatically and spam them into a chat, either as:

- a webhook message generated from random words and a chosen article title
- or a proper Discord bot that responds to a channel event

This reflects the dojo's love of chaotic but creative automation: generate weird project suggestions, then let a bot deliver them as if they were commands from a tyrannical AI overlord.

## Output

The result is a Discord message such as:

```text
I, the Almighty Ruler, command you to build a Privacy Invader
```

or some similarly absurd task suggestion. Group 2's output is more interactive: it logs into the Discord server and replies when messages are sent.

The user-facing success condition is therefore simple: the bot appears in the chat and/or sends a new random challenge suggestion to the channel.

## Summary

This session combines two patterns: idea generation and bot automation. Group 1 builds a random challenge generator that posts to Discord; Group 2 creates a bot client that can listen for events and respond in a chat. Together, they demonstrate a lightweight approach to automation: generate creative prompts, then send them to a collaborative platform where people can react to them.

The code is clearly experimental and not production-ready, but it captures the exact type of playful automation the dojo often tries: weird prompts, random inspiration, and a bit of Discord chaos.
