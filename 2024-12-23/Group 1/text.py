
START_SESSION_HELP = (
"""Attempts to start a session by doing the following:
* Counting the users who have sent a message in "Ideas" Within the past hour
* if > 6 will attempt to split them into two groups with even experience
* sends messages to group 1 and group 2
* Creates codespace(s). WIP
This command is only available for those with the sensei role.
"""
)

DOJO_MEETUP_LINK = ""
HACKNIGHT_MEETUP_LINK = ""
DECODERING_INVITE = ""
HACKNIGHT_LINK = ""

def make_codehub_explination_text(*,
                                  event_command = "calender",
                                  decodering_invite = DECODERING_INVITE,
                                  dojo_link = DOJO_MEETUP_LINK,
                                  hacknight_link = HACKNIGHT_MEETUP_LINK):
    return f"""Codehub are a charity organisation that hosts the [Python Dojo]({dojo_link}) every other Wednesday
as well as [Decodering]({decodering_invite}) the day before and [Hacknight]({hacknight_link}) 
every alternating Tuesday. Use !{event_command} to get a calender view of events.
"""

# Discord doesn't support tables so use a codeblock that looks like a table
EVENT_CALENDER_TABLE = (
"""```Markdown
+----------------------------------------------------------+
| Week | Mon | Tuesday | Wednesday | Thu | Fri | Sat | Sun |
+------+-----+---------+-----------+-----+-----+-----+-----|
|   1  |     | Decoder | Dojo / WW |     |     |     |     |
+------+-----+---------+-----------+-----+-----+-----+-----|
|   2  |     | Hacknig |           |     |     |     |     |
+----------------------------------------------------------+
```"""
)