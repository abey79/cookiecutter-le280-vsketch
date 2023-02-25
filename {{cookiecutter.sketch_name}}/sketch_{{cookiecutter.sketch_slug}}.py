import vsketch

import vpype as vp


class {{cookiecutter.class_name}}(vsketch.SketchClass):
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        # Your code here

        vsk.vpype("color black crop 0 0 500 500")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right {{cookiecutter.sketch_name}} "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linemerge linesimplify reloop linesort"
        )


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
