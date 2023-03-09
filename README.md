# Guide

- [Guide](#guide)
  - [: Developers Guide](#-developers-guide)
    - [:: Requirements](#-requirements)
    - [:: Onboard Procedure](#-onboard-procedure)
    - [:: Conclusion](#-conclusion)
    - [:: Other Useful Gotchas](#-other-useful-gotchas)
    - [:: Statement Of Intent](#-statement-of-intent)

## : Developers Guide

### :: Requirements

**LEGEND** ❯ <-- MarioKart SpeedBump symbol signifies a terminal command.

There are **TWO** major requirements before proceeding.
One is **pyenv**, which is my preferred python environment manager, which helps migration and switching to newer versions of python. The other is **poetry** which is a package manager to increase the developer experience, provide basic scripting access, and package organization. There installation guides can be found on their `github`. I, myself install pyenv via brew, and with poetry, I use pip (it is recommended on their site to keep the poetry dependency in a pyenv virtualenv, and allow the poetry virtualenv to handle/house the dependencies )

The following is a list of commands in timeline format (one would do them procedurally).

* `pyenv` :
  * `❯ pyenv install 3.9.4` (or whatever version I've specified)
    * M1 Macs don't support all versions. 3.9.4 is the least buggy.
    * Any updates to this will be found in the .python-version
  * `❯ pyenv virtualenv 3.9.4 3.9.4-poetry-starter`
    * There has to be an python virtualenv for poetry to initially run on.
  * `❯ source deactivate`
    * Deactivates pyenv
  * You can confirm you virtualenv environment at anytime with a `❯ which python` or `❯ which pip`

* `❯ poetry` : <--->
  * The following lists the commonly used command for poetry:
    * starters
      * `❯ poetry shell`
        * Activates the shell AND the default virtualenv.
        * `❯ which pip`
          * IF pip path resembles:
            * `❯ gpt-experiment-J4ujJ6jN-py3.9`
              * THEN virtualenv has activated, as expected.
          * IF pip path resembles:
            * `❯ [❯HOME]/.pyenv/shims/pip`
              * THEN virtualenv needs to be initialized (only once)
              * To initialize the virtualenv once:
                * `❯ poetry env use ❯(poetry env info --path)`
                * `❯ poetry env info --path` gives you info on your poetry virtualenv path. It output should resemble:
                  * `❯ [❯HOME]/Library/Caches/pypoetry/virtualenvs/gpt-experiment-J4ujJ6jN-py3.9`
      * `❯ poetry env list`
        * Provides a readout of all your poetry `virtualenvs`. Helps confirm that you have activated your poetry virtualenv
      * `poetry env info --path`
        * confirm that you are using the correct virtualenv
    * `❯ poetry install`
      * Installs all the dependencies in the cargo `toml` file;
    * `❯ poetry cache list`
    * `❯ poetry cache remove`
    * `❯ exit`
      * Deactivates shell.
      * `❯ deactivate`
        * Deactivates poetry's virtualenv.
      * `which pip`
        * pip's location will have changed with the deactivation.j

By now your **`virtualenvs`** should be set up, and you are ready for onboarding.

### :: Onboard Procedure

* Step 1 (Add Auto-formatting!):
  * Install black extension for vscode
  * type `❯ poetry install` to install all poetry dependencies.
  * Setup the vscode workspace settings.
    ```json
    {
      "editor.defaultFormatter": null,
      "python.formatting.provider": "black",
      "python.formatting.blackPath": "INSERT DARKER LOCATION",
      "python.formatting.blackArgs": [],
      "editor.formatOnSave": true,
      "python.linting.flake8Enabled": true,
      "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "ms-python.black-formatter"
      },
      "python.terminal.activateEnvInCurrentTerminal": true,
      // "python.poetryPath": "poetry"
    }
    ```
  * Step 1 (Explanations):
    * `Black` will the auto-formatter of choice for the `vscode IDE`;
    * The workspace settings is to improve developer experiences, and is optional.
      * Explanation of `darker`
        * When you install darker, black and other `deps` come along for the ride.
          * You can see the full list in requirements, such as `mypi` and `isort`.
            * Run `❯ pip freeze > requirements` to see
        * darker is used for per line formatting based on git diffs.
* ...TO BE CONTINUED...
  * Step 2: SCRIPTS (POE) ...TO BE CONTINUED...
  * Step 3: TESTING (TOX) ...TO BE CONTINUED...
  * Step 4: VERSIONING + CHANGELOG ...TO BE CONTINUED...
  * Step 5: CONVENTIONAL COMMITS ...TO BE CONTINUED...
  * Step 6: DOCUMENTATION ...TO BE CONTINUED...
  * Step 7: PROJECT PLANNING ...TO BE CONTINUED...
  * Step 8: DEPLOYMENT ...TO BE CONTINUED...
  * Step 9: CI/CD ...TO BE CONTINUED...

### :: Conclusion

Now that the `virtualenvs` are ready, the dependencies are all installed, development should be straight forward.

`❯ poetry run start` is the rudimentary start script.

### :: Other Useful Gotchas

* `❯ poetry add [dep] -D`
  * Installs a dependency to the dev group in the `toml` file.
    * KEEP in mind that this command only works for `Python 3.9.4`
    * In later versions of python (3.10 and 3.11), poetry uses the `--group [GROUPNAME]` (aka posix long option argument), instead.
* Make sure that you know what virtualenv you are in.(some helpful options for you to determine your virtualenv)
  * `❯ pip list freeze > requirements.txt`
    * If you don't see any overwrites, then you prolly on the same virtualenv.
  * `❯ pip list | less`
    * Page your dependencies without overwriting the requirements.txt.
    * If it looks short and familiar, it ain't wrong.
* `❯ pip list | grep poetry`
  * You shouldn't have any poetry dependencies in your poetry-managed virtualenv.
  * If you do, you are installing `deps` in the wrong place.

---

### :: Statement Of Intent

These are in no order of importance.

* [ ] Explore GPT
* [ ] Explore Linear Algebra
* [ ] Explore Transformers
* [ ] Retain Python Fluency
