# Python Discord Code Jam Repository Template

## A primer

Hello code jam participants! We've put together this repository template for you to use in [our code jams](https://pythondiscord.com/events/) or even other Python events!

This document contains the following information:

1. [What does this template contain?](#what-does-this-template-contain)
2. [How do I use this template?](#how-do-i-use-this-template)
3. [How do I adapt this template to my project?](#how-do-i-adapt-this-template-to-my-project)

> [!TIP]
> You can also look at [our style guide](https://pythondiscord.com/events/code-jams/code-style-guide/) to get more information about what we consider a maintainable code style.

## What does this template contain?

Here is a quick rundown of what each file in this repository contains:

- [`LICENSE.txt`](LICENSE.txt): [The MIT License](https://opensource.org/licenses/MIT), an OSS approved license which grants rights to everyone to use and modify your project, and limits your liability. We highly recommend you to read the license.
- [`.gitignore`](.gitignore): A list of files and directories that will be ignored by Git. Most of them are auto-generated or contain data that you wouldn't want to share publicly.
- [`requirements-dev.txt`](requirements-dev.txt): Every PyPI package used for the project's development, to ensure a common development environment. More on that [below](#using-the-default-pip-setup).
- [`pyproject.toml`](pyproject.toml): Configuration and metadata for the project, as well as the linting tool Ruff. If you're interested, you can read more about `pyproject.toml` in the [Python Packaging documentation](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
- [`.pre-commit-config.yaml`](.pre-commit-config.yaml): The configuration of the [pre-commit](https://pre-commit.com/) tool.
- [`.github/workflows/lint.yaml`](.github/workflows/lint.yaml): A [GitHub Actions](https://github.com/features/actions) workflow, a set of actions run by GitHub on their server after each push, to ensure the style requirements are met.

Each of these files have comments for you to understand easily, and modify to fit your needs.

### Ruff: general style rules

Our first tool is Ruff. It will check your codebase and warn you about any non-conforming lines.
It is run with the command `ruff check` in the project root.

Here is a sample output:

```shell
$ ruff check
app.py:1:5: N802 Function name `helloWorld` should be lowercase
app.py:1:5: ANN201 Missing return type annotation for public function `helloWorld`
app.py:2:5: D400 First line should end with a period
app.py:2:5: D403 First word of the first line should be capitalized: `docstring` -> `Docstring`
app.py:3:15: W292 No newline at end of file
Found 5 errors.
```

Each line corresponds to an error. The first part is the file path, then the line number, and the column index.
Then comes the error code, a unique identifier of the error, and then a human-readable message.

If, for any reason, you do not wish to comply with this specific error on a specific line, you can add `# noqa: CODE` at the end of the line.
For example:

```python
def helloWorld():  # noqa: N802
    ...

```

This will ignore the function naming issue and pass linting.

> [!WARNING]
> We do not recommend ignoring errors unless you have a good reason to do so.

### Ruff: formatting

Ruff also comes with a formatter, which can be run with the command `ruff format`.
It follows the same code style enforced by [Black](https://black.readthedocs.io/en/stable/index.html), so there's no need to pick between them.

### Pre-commit: run linting before committing

The second tool doesn't check your code, but rather makes sure that you actually *do* check it.

It makes use of a feature called [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) which allow you to run a piece of code before running `git commit`.
The good thing about it is that it will cancel your commit if the lint doesn't pass. You won't have to wait for GitHub Actions to report issues and have a second fix commit.

It is *installed* by running `pre-commit install` and can be run manually by calling only `pre-commit`.

[Lint before you push!](https://soundcloud.com/lemonsaurusrex/lint-before-you-push)

#### List of hooks

- `check-toml`: Lints and corrects your TOML files.
- `check-yaml`: Lints and corrects your YAML files.
- `end-of-file-fixer`: Makes sure you always have an empty line at the end of your file.
- `trailing-whitespace`: Removes whitespaces at the end of each line.
- `ruff`: Runs the Ruff linter.
- `ruff-format`: Runs the Ruff formatter.

## How do I use this template?

### Creating your team repository

One person in the team, preferably the leader, will have to create the repository and add other members as collaborators.

1. In the top right corner of your screen, where **Clone** usually is, you have a **Use this template** button to click.
   ![use-this-template-button](https://docs.github.com/assets/images/help/repository/use-this-template-button.png)
2. Give the repository a name and a description.
   ![create-repository-name](https://docs.github.com/assets/images/help/repository/create-repository-name.png)
3. Click **Create repository from template**.
4. Click **Settings** in your newly created repository.
   ![repo-actions-settings](https://docs.github.com/assets/images/help/repository/repo-actions-settings.png)
5. In the "Access" section of the sidebar, click **Collaborators**.
   ![collaborators-settings](https://github.com/python-discord/code-jam-template/assets/63936253/c150110e-d1b5-4e4d-93e0-0a2cf1de352b)
6. Click **Add people**.
7. Insert the names of each of your teammates, and invite them. Once they have accepted the invitation in their email, they will have write access to the repository.

You are now ready to go! Sit down, relax, and wait for the kickstart!

> [!IMPORTANT]
> Don't forget to swap "Python Discord" in the [`LICENSE.txt`](LICENSE.txt) file for the name of each of your team members or the name of your team *after* the start of the code jam.

### Using the default pip setup

Our default setup includes a bare requirements file to be used with a [virtual environment](https://docs.python.org/3/library/venv.html).
We recommend this if you have never used any other dependency manager, although if you have, feel free to switch to it. More on that [below](#how-do-i-adapt-this-template-to-my-project).

#### Creating the environment

Create a virtual environment in the folder `.venv`.

```shell
python -m venv .venv
```

#### Entering the environment

It will change based on your operating system and shell.

```shell
# Linux, Bash
$ source .venv/bin/activate
# Linux, Fish
$ source .venv/bin/activate.fish
# Linux, Csh
$ source .venv/bin/activate.csh
# Linux, PowerShell Core
$ .venv/bin/Activate.ps1
# Windows, cmd.exe
> .venv\Scripts\activate.bat
# Windows, PowerShell
> .venv\Scripts\Activate.ps1
```

#### Installing the dependencies

Once the environment is created and activated, use this command to install the development dependencies.

```shell
pip install -r requirements-dev.txt
```

#### Exiting the environment

Interestingly enough, it is the same for every platform.

```shell
deactivate
```

Once the environment is activated, all the commands listed previously should work.

> [!IMPORTANT]
> We highly recommend that you run `pre-commit install` as soon as possible.

## How do I adapt this template to my project?

If you wish to use Pipenv or Poetry, you will have to move the dependencies in [`requirements-dev.txt`](requirements-dev.txt) to the development dependencies of your tool.

We've included a porting of [`requirements-dev.txt`](requirements-dev.txt) to both [Poetry](samples/pyproject.toml) and [Pipenv](samples/Pipfile) in the [`samples` folder](samples).
If you use the Poetry setup, make sure to change the project name, description, and authors at the top of the file.
Also note that the Poetry [`pyproject.toml`](samples/pyproject.toml) file does not include the Ruff configuration, so if you simply replace the file then the Ruff configuration will be lost.

When installing new dependencies, don't forget to [pin](https://pip.pypa.io/en/stable/topics/repeatable-installs/#pinning-the-package-versions) them by adding a version tag at the end.
For example, if I wish to install [Click](https://click.palletsprojects.com/en/8.1.x/), a quick look at [PyPI](https://pypi.org/project/click/) tells me that `8.1.7` is the latest version.
I will then add `click~=8.1`, without the last number, to my requirements file or dependency manager.

> [!IMPORTANT]
> A code jam project is left unmaintained after the end of the event. If the dependencies aren't pinned, the project will break after any major change in an API.

## Final words

> [!IMPORTANT]
> Don't forget to replace this README with an actual description of your project! Images are also welcome!

We hope this template will be helpful. Good luck in the jam!
