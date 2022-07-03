import nox

locations = "blockscan", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.9", "3.10"])
def tests(session):
    session.install("-e", ".")
    session.install("-r", "tests/requirements.txt")
    session.run("pytest")


@nox.session(reuse_venv=True, python="3.10")
def black(session):
    """Run black code formatter."""

    session.install("black")
    session.run("black", *locations)


@nox.session(reuse_venv=True, python="3.10")
def lint(session):
    session.install("flake8", "black")
    session.run("flake8", "--version")
    session.run("black", "--version")
    session.run("black", "--check", *locations)
    session.run("flake8", *locations)


@nox.session(reuse_venv=True, python="3.10")
def docs(session):
    session.install("-e", ".")
    session.install("-r", "docs/requirements.txt")

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-W", "-b", "html", "-v", "docs/", "docs/_build/html")
