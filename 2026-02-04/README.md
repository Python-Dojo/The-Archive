# Task

Search a small collection of online documents for one or more terms, then rank the documents using TF-IDF (term frequency–inverse document frequency).

## What the program does

The script in `Group-1/main.py` downloads README files from a fixed set of GitHub projects. It tokenises each document into lowercase words, counts the words per document, and calculates a relevance score for the search terms supplied on the command line.

For each document, the score adds the term-frequency value for each query term multiplied by that term's inverse-document-frequency value. The documents are then sorted from highest score to lowest and printed with their URLs.

## Main concept

TF-IDF combines two signals:

- **Term frequency (TF):** how often a term appears in a document relative to all its tokens.
- **Inverse document frequency (IDF):** how uncommon the term is across the collection.

A term can therefore be important to a document when it appears frequently there but is less common in the other documents. The implementation uses smoothing in its IDF calculation so that terms absent from every document do not cause a division-by-zero error.

## Output and limitations

Run the script with search terms as arguments, for example:

```bash
python main.py rust package
```

It prints each source URL and its score in descending order. The program fetches the whole fixed corpus each time it runs; it does not search arbitrary files or accept document URLs as command-line options.

The prototype does not check HTTP status codes or handle network failures. It converts response bytes to a Python string representation rather than decoding the response as text, which can affect tokenisation. It also reports all documents, including those with a zero score.

## Summary

This project is a small document-ranking experiment. It downloads a set of project READMEs, computes TF-IDF scores for the requested terms, and prints a ranked list of source documents. It demonstrates the core relevance-scoring idea, while leaving robust fetching, text decoding, and broader corpus selection for future work.
