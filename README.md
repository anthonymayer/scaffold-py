# Scaffold for Python

This project is a fork of https://github.com/Aaronontheweb/scaffold-py. The goal is to make it as DRY as possible to setup and maintain a python package with a baseline of utilities ready to go. Current utilities include [pre-commit](http://pre-commit.com/), [tox](https://tox.readthedocs.org), [flake8](http://flake8.readthedocs.org/), [pytest](http://pytest.org/), and more. These utilities were picked as a baseline, but the plan is to make the scaffolded utilities configurable and make it easy to add more.

Each project you scaffold will create the following directory structure:

```
/[projectname]/
/[projectname]/.coveragerc
/[projectname]/.gitattributes
/[projectname]/.gitignore
/[projectname]/.pre-commit-config.yaml
/[projectname]/Makefile
/[projectname]/pylintrc
/[projectname]/requirements-dev.txt
/[projectname]/setup.py
/[projectname]/tox.ini
/[projectname]/[projectname]
/[projectname]/[projectname]/__init__.py
/[projectname]/tests
/[projectname]/tests/__init__.py

```

`setup.py` and `tox.ini` are set up automatically to reference your project name.

## Running Scaffold

Scaffold installs itself as an executable Python script, so just enter the `pyscaffold` command on your favorite terminal:

```
pyscaffold -p "projectname" [-d {base directory}]
```

You can also run scaffold as a python module if needed:

```
python -m scaffold -p "projectname" [-d {base directory}]
```

The `-p` parameter is the name of your project and is a required field. If you don't specify a base directory with the `-d` parameter, scaffold will assume that you want to create your project skeleton in your current working directory.

### Sample Usage

Just to give you an idea of what works and what doesn't...

```
pyscaffold -p "http-utils" -d /c/repositories/
pyscaffold -p "mutliplex-py"
pyscaffold -p "lazarus" -d ../
```

## Virtualenvwrapper support

Alternatively, if (the excellent) [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org) is installed, Scaffold also works as a [project template](https://virtualenvwrapper.readthedocs.org/en/latest/projects.html#using-templates) named _base_. So you could run:

```
mkproject -t base projectname
```

Then virtualenvwrapper will create the virtualenv and the project root and Scaffold will do the rest.

## License

Licensed under Apache 2.0 - see license.txt for details.

## Contribution

Pull requests are extremely welcome.

## Ideas
- Instead of generating all the necessary static files for a project, generate some sort of very lightweight files that would then be combined with base files from a package. That way if base configurations changed, the package could just be bumped and include anything new.
- Add an update command that would figure out the state of the project, update any configuration files, and add any new ones.
- Build an entire package management service that would combine some local configuration with some remote base configuration.
- Some sort of integration with [pip-tools](https://github.com/nvie/pip-tools) to manage out of date dependencies. Could be as simple as a pip-tools [pre-commit hook](http://pre-commit.com/#new-hooks).
