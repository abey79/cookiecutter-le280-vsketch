import vsketch


class {{cookiecutter.class_name}}(vsketch.Vsketch):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self) -> None:
        self.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
        self.scale("{{cookiecutter.preferred_unit}}")

        # implement your sketch here
        # self.circle(0, 0, self.radius(), mode="radius")

    def finalize(self) -> None:
        self.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    vsk = {{cookiecutter.class_name}}()
    vsk.draw()
    vsk.finalize()
    vsk.display()