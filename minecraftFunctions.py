import subprocess

import minecraft_launcher_lib


def runGame():
    options = minecraft_launcher_lib.utils.generate_test_options()
    mcCommand = minecraft_launcher_lib.command.get_minecraft_command("fabric-loader-0.15.7-1.20.1", "mc", options)
    subprocess.call(mcCommand)
