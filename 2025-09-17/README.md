# Task

Scrape crossword clues and solutions from The Guardian's crossword pages, convert the page data into structured records, and store those records in SQLite.

## What the programs do

The main work is in `Group-1`. Its `main.py` defines a `Clue` dataclass containing a crossword ID, clue number, clue text, solution, and direction. A `DataBase` class creates a SQLite table and provides methods to insert clues and retrieve stored rows.

The scraper in `ray.py` outlines the web-data pipeline:

1. Request The Guardian crossword landing page.
2. Parse crossword links with Beautiful Soup.
3. Fetch crossword pages and read the embedded crossword component data.
4. Parse the JSON entries into `Clue` objects.
5. Add the clues to a database.

The same directory includes experiments by several participants. `michael.py` sketches database tests using sample clues; `scott.py` contains a basic site request and parsing experiments; the other files are incomplete or exploratory attempts. The `Ray/main.py` file is another scraper-and-database version that develops the parsing and persistence flow further.

## Main concept

The task is to turn semi-structured web content into durable, queryable data. Beautiful Soup is used to locate page links and embedded crossword data, a dataclass gives each clue a predictable shape, and SQLite provides storage for the extracted clues.

The design separates scraping, parsing, and persistence so that clue data can be tested independently from the live website. The sample clues and mock database are intended to support that testing.

## Output and limitations

The intended output is a SQLite database containing crossword clues, their solutions, direction, and crossword identifiers. The more complete script also prints the rows retrieved from the database and writes the most recently extracted page data to `out.json`.

This is a prototype, not a dependable scraper: some group files are unfinished, the live page structure may change, and the database creation code uses a plain `CREATE TABLE` rather than handling an existing table. Network requests also lack robust error handling. The archived scripts may require adjustment before they run end to end.

## Summary

This session explores a full data-ingestion path for crosswords: fetch pages, extract embedded puzzle data, parse clues into typed records, and save them in SQLite. Its intended result is a local crossword clue database, with the archived code capturing the architecture and several partial implementations rather than a polished scraper.
