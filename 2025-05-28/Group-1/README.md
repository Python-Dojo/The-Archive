
# Do regex expression over diff for each file as a precommit linting hook

Git accepts a pre commit hook which runs on a exe before commiting

It does some check on the codebase's staged changes


## What we learned
- File in `.git/hook` must be chmod'd to be executable
- You cannot symlink the file in the `.git/hook`s folder it needs to be an actual file
    + You can use a hard link instead! (https://archive.is/VhYth)

## How to make a precommit hook
- Create an executable file (e.g. python file with shebang added, `#!/usr/bin/env python3`)
- Put that file in .git/hooks and call it `pre-commit`
    + Note that this name is specific, it cannot be `precommit` or `pre-commit.py` it *must* be `pre-commit` alone
- Provide the permissions with
    ```bash
    chmod +x .git/hooks/precommit
    ```
- Add your changes, try to commit and watch the magic
