import pathlib

HERE = pathlib.Path(__file__).parent
BUILD_DIR = HERE / "site" / ".vuepress" / "dist"
GENERATED_DIR = HERE / "site" / ".vuepress" / "generated"

assert (
    BUILD_DIR.exists() and GENERATED_DIR.exists()
), "Blog site hasn't been built yet. HINT: $ scripts/build"