from typing import Optional

from cleo import argument
from cleo import option

from poetry.utils._compat import Path

from ..command import Command


class BundleVenvCommand(Command):

    name = "venv"
    description = "Bundle the current project into a virtual environment"

    arguments = [
        argument("path", "The path to the virtual environment to bundle into."),
    ]

    options = [
        option(
            "python",
            "p",
            "The Python executable to use to create the virtual environment. "
            "Defaults to the current Python executable",
            flag=False,
            value_required=True,
        ),
        option(
            "clear",
            None,
            "Clear the existing virtual environment if it exists. ",
            flag=True,
        ),
    ]

    def handle(self):  # type: () -> Optional[int]
        from poetry.bundle import bundler_manager

        path = Path(self.argument("path"))
        executable = self.option("python")

        bundler = bundler_manager.bundler("venv")

        self.line("")

        return int(
            not bundler.bundle(
                self.poetry,
                self._io,
                path,
                executable=executable,
                remove=self.option("clear"),
            )
        )
