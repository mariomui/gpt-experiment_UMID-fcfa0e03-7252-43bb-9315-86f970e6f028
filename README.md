# Guide

## : Developers Guide

### :: Requirements

* make sure you have poetry.
* Step 1
  * install black extension
  * poetry install
  * vscode workspace settings.
    ```json
    {
      "editor.defaultFormatter": null,
      "python.formatting.provider": "black",
      "python.formatting.blackPath": "INSERT DARKER LOCATION",
      "editor.formatOnSave": true,
      "python.linting.flake8Enabled": true,
      "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "ms-python.black-formatter"
      },
      "python.terminal.activateEnvInCurrentTerminal": false,
      // "python.poetryPath": "poetry"
    }
    ```
* Step 1 explanations
  * basically we are using black, the extension and then overwriting it with darker.
  * Darker allows per git code formatting allowing per line formatting, rather than formatting per file.
    * Anything I change will be formatted my way to avoid crime-scene like PRs.
