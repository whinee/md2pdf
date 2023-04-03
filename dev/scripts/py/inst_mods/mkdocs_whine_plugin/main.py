import re
from typing import Optional

import jinja2
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files

RE_TOC_FA = re.compile(r'<div class="toc">.+?<\/div>', re.MULTILINE | re.DOTALL).findall
RE_TOC_H2_FA = re.compile(r'<h2 id="toc">.+?<\/h2>', re.MULTILINE | re.DOTALL).findall


def get_toc(md):
    res = False
    op = ""
    if op := RE_TOC_FA(md):
        res = True
        op = op[0]
        md = md.replace(op, "", 1)
        op = op.replace(RE_TOC_H2_FA(op)[0], "", 1)
    return res, op, md


class MainPlugin(BasePlugin):
    # def on_config(self, config: MkDocsConfig) -> Optional[Config]:

    def on_env(
        self,
        env: jinja2.Environment,
        *,
        config: MkDocsConfig,
        files: Files,
    ) -> Optional[jinja2.Environment]:
        env.filters["get_toc"] = get_toc
        return env

    # def on_template_context(
    #     self, context: dict[str, Any], *, template_name: str, config: MkDocsConfig
    # ) -> Optional[dict[str, Any]]:
    #     print(template_name)
    #     pprint(context)
