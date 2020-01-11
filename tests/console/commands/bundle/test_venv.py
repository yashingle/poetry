from cleo.testers import CommandTester

from poetry.utils._compat import Path


def test_venv_calls_venv_bundler(app, mocker):
    mock = mocker.patch(
        "poetry.bundle.venv_bundler.VenvBundler.bundle", side_effect=[True, False]
    )
    command = app.find("bundle venv")
    tester = CommandTester(command)

    assert 0 == tester.execute("/foo")
    assert 1 == tester.execute("/foo --python python3.8 --clear")

    assert [
        mocker.call(
            command.poetry, command.io, Path("/foo"), executable=None, remove=False
        ),
        mocker.call(
            command.poetry,
            command.io,
            Path("/foo"),
            executable="python3.8",
            remove=True,
        ),
    ] == mock.call_args_list
