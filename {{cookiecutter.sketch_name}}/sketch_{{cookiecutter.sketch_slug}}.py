import vsketch


class {{cookiecutter.class_name}}(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
        vsk.scale("{{cookiecutter.preferred_unit}}")

        # implement your sketch here
        # vsk.circle(0, 0, self.radius(), mode="radius")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
