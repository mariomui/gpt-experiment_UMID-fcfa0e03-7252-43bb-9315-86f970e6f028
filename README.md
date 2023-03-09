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
      "python.formatting.blackPath": "INSERT BLACK LOCATION",
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
