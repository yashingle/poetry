from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Optional

    from clikit.api.io.io import IO
    from poetry.poetry import Poetry
    from poetry.utils._compat import Path


class Bundler(object):
    @property
    def name(self):  # type: () -> str
        raise NotImplementedError()

    def bundle(
        self, poetry, io, path, executable=None
    ):  # type: (Poetry, IO, Path, Optional[str]) -> None
        raise NotImplementedError()
