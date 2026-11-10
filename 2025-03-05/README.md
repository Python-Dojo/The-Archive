# Task

Prepare a “right to be forgotten” email and send it to data brokers, exercising the sender's GDPR erasure rights.

## What the program does

The main prototype in `Group-1/main.py` reads the message body from `email_contents.txt`, obtains the sender address from the `USER_EMAIL` environment variable (with a local-file fallback), and builds an email with the subject “GDPR Right to be forgotten.” It then uses Google's Gmail API client to send the message.

The same group includes `reader.py`, which reads email addresses from a CSV file, and a separate `csv_test.py` experiment for extracting the first column. These scripts explore sourcing recipients from a list, but the main Gmail function currently uses a single hard-coded recipient rather than connecting the CSV reader to the send operation.

`Group-2` contains several small SMTP experiments. They explore composing messages and sending them through Gmail or a local SMTP server, but some files are unfinished and contain missing configuration values.

## Main concept

The central idea is to automate the repetitive parts of sending a privacy request: keep the request text in a file, obtain a list of recipient addresses from CSV data, construct a properly headed email, and deliver it through an email service.

The examples compare two sending approaches:

- Gmail's API, which requires Google authentication and an API client.
- SMTP, which connects to a mail server and sends an `EmailMessage`.

These are exploratory pieces rather than one integrated mailing application. The recipient reader, message construction, and delivery flow are not yet fully connected.

## Intended output

The intended result is an email containing the request text, addressed to a data broker, asking for the sender's personal data to be erased. The Gmail API example prints the returned message ID after a successful send; the SMTP examples attempt delivery through their configured server.

## Summary

This session explores how to read a set of email addresses, compose a GDPR erasure request, and send it using Python email tooling. The archived work demonstrates CSV parsing, email message construction, Gmail API usage, and SMTP, but it does not yet provide a complete, ready-to-run bulk-mail workflow. Check recipients and configuration carefully before sending any real requests.
