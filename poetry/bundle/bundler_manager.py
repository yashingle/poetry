from typing import Dict
from typing import List

from .bundler import Bundler
from .exceptions import BundlerManagerError
from .venv_bundler import VenvBundler


class BundlerManager(object):
    def __init__(self):  # type: () -> None
        self._bundlers = {}  # type: Dict[str, Bundler]

        # Register default bundlers
        self.register_bundler(VenvBundler())

    @property
    def bundlers(self):  # type: () -> List[Bundler]
        return list(self._bundlers.values())

    def bundler(self, name):  # type: (str) -> Bundler
        if name.lower() not in self._bundlers:
            raise BundlerManagerError('The bundler "{}" does not exist.'.format(name))

        return self._bundlers[name.lower()]

    def register_bundler(self, bundler):  # type: (Bundler) -> BundlerManager
        if bundler.name.lower() in self._bundlers:
            raise BundlerManagerError(
                'A bundler with the name "{}" already exists.'.format(bundler.name)
            )

        self._bundlers[bundler.name.lower()] = bundler
