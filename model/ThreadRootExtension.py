# TODO: Enable \r\n to <br /> support (no more reddit spacing)
from markdown import Extension

from model.ThreadPostProcessor import ThreadPostprocessor


class ThreadRootExtension(Extension):
    def extendMarkdown(self, md, _):
        md.postprocessors.add("threadroot", ThreadPostprocessor(), "_end")
