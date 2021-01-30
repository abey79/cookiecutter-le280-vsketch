import vsketch


def setup(vsk: vsketch.Vsketch) -> None:
    vsk.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
    vsk.scale("{{cookiecutter.preferred_unit")


def draw(vsk: vsketch.Vsketch) -> None:
    pass


def finalize(vsk: vsketch.Vsketch) -> None:
    vsk.vpype("linemerge linesort")
