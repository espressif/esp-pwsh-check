# Contributing and Development

We welcome contributions! To contribute to this repository, please follow these steps:

## Code and Testing

- **Code Style and Structure:**

- **Pre-Commit Hooks:** Install pre-commit hooks in this repository using the `pre-commit install` command.

- **Readable Code Structure:** Structure your code in a readable manner. The main logic should be in the default rule function, with implementation details in helper functions. Avoid nested `if` statements and unnecessary `else` statements to maintain code clarity and simplicity.

- **Remove Debug Statements:** Remove any development debug statements from your files.


## Documentation and Maintenance

- **Changelog:** `CHANGELOG.md` is generated automatically by `commitizen` from commit messages. No need to update `CHANGELOG.md` manually. Focus on informative and clear commit messages that end in the release notes.

- **Documentation:** Regularly check and update the documentation to keep it current.

- **PR Descriptions and Documentation:** When making contributions, clearly describe any changes or new features in the PR (Pull Request on GitHub) description and the project documentation. If you're modifying the output style, please include a thumbnail of the new style.

## Development and Local Testing

1. **Clone the Project**

- Clone the repository to your local machine using:

```sh
git clone <project_clone_url>
```

2. **Set Up Development Environment:**

- Create and activate a virtual environment:

  ```sh
  python -m venv venv && source ./venv/bin/activate
  ```

  or:

  ```sh
  virtualenv venv && source ./venv/bin/activate
  ```

- Install the project and development dependencies:
  ```sh
  pip install -e '.[dev]'
  ```

3. **Test the pre-commit hook locally:**
  - Test the local hook of this repository in a different repository with the use of the following command

  ```sh
  pre-commit try-repo <path_to_this_repo> <hook_name>
  ```
  for example:
   ```sh
  pre-commit try-repo ../esp_pwsh_check check-powershell-scripts
  ```

---

👏**Thank you for your contributions.**
