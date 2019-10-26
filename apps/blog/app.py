import pathlib

from starlette.staticfiles import StaticFiles
from starlette.types import Receive, Scope, Send

HERE = pathlib.Path(__file__).parent
BUILD_DIR = HERE / "site" / ".vuepress" / "dist"
assert (
    BUILD_DIR.exists()
), "Blog site hasn't been built yet. HINT: run `$ scripts/build`."

static = StaticFiles(directory=str(BUILD_DIR))


async def app(scope: Scope, receive: Receive, send: Send) -> None:
    if scope["path"] == "/":
        scope["path"] = "/index.html"
    await static(scope, receive, send)