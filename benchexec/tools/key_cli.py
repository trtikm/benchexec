import re
from pathlib import Path

from benchexec.tools import template


class Tool(template.BaseTool2):
    """
    This tool-info module runs Cheetah, a parallel portfolio
    of natively compiled CPAchecker instances.
    """

    REQUIRED_PATHS = ["bin", "lib"]

    def executable(self, tool_locator):
        return tool_locator.find_executable("key-cli", subdir="bin")

    def version(self, executable):
        lib = Path(executable).parent.parent / "lib"
        for file in lib.glob("key-*-exe.jar"):
            match = re.match(r"key-(.*)-exe.jar", file.name)

            if match:
                return match.group(1)

        return "unknown"

    def program_files(self, executable):
        return self._program_files_from_executable(
            executable, self.REQUIRED_PATHS, parent_dir=True
        )

    def name(self):
        return "KeY"

    def cmdline(self, executable, options, task, rlimits):
        return super().cmdline(executable, options, task, rlimits)
