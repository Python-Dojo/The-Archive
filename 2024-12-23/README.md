# Task

Build a Discord bot to help run the Python Dojo by tracking active users, looking up experience, and starting a session by splitting people into groups.

This folder contains a Python bot prototype from the 2024-12-23 session. The project is focused on automation for event management in Discord: identify active participants, gather their experience levels, and use that data to create balanced session groups.

## What the program does

The implementation in `Group 1/main.py` creates a Discord bot using the `discord.py` library. It reads configuration from environment variables, registers bot commands, and accesses specific Discord channels by ID.

The bot includes a `start_session` command that does the following:

- looks at recent messages in a welcome channel and idea channel
- finds users who have been active recently
- collects their experience data from a database channel
- determines which users should be grouped together for the next session

This is a session-management system rather than a game or utility script. The output is meant to be a group assignment or organizer workflow inside the Discord server.

## Main concept

The core idea is to combine activity tracking with user experience tracking.

The code defines helper functions such as:

- `get_active_users(...)`: scan channel history and collect anyone who has posted recently or reacted to messages
- `get_user_experience(...)`: parse messages in a database channel that map user IDs to “experience” values

This means the bot is trying to treat the server as a lightweight social graph: active members are discovered from message history, and their skill/experience is inferred from a stored ranking channel.

The command then uses that data to split the group into session teams. It is still a skeleton, but the design is clear: gather data -> compute group membership -> organise the session.

## Output

The bot is intended to produce practical Discord-side outcomes:

- a session start command
- messages in a channel describing the event calendar
- information about codehub / events
- group assignments based on recent activity and user experience

The session bot is therefore meant to provide organiser tooling, not a finished user-facing game.

## Summary

This project is a prototype Discord ops bot for the dojo. It tracks activity, parses user experience data, and provides infrastructure for starting and managing group sessions. It is a useful example of automation for community coordination: using channel history as a source of user activity and then turning that into team formation logic.

The code is intentionally incomplete and still structured as a work-in-progress, but the task itself is clear and practical: make the dojo easier to run by automatically identifying people and assigning them into balanced groups.
