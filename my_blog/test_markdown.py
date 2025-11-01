#!/usr/bin/env python3
# 最小脚本：直接用内置示例，把 Markdown 转为带 Pygments 高亮的 HTML，并打印到控制台

import markdown
from pygments.formatters import HtmlFormatter

SAMPLE_MD = """# 示例 Markdown

这是一个内置的测试文档，包含代码块以测试 Pygments 高亮。

```python
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```

也支持其他语言：

```javascript
function greet(name) {
  console.log("Hello, " + name + "!");
}
greet("World");
```
"""

def render_markdown(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=['fenced_code', 'codehilite'],
        extension_configs={'codehilite': {'linenums': False, 'guess_lang': False}}
    )
    css = HtmlFormatter().get_style_defs('.codehilite')
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Markdown → Highlighted HTML</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; padding: 20px; }}
{css}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

if __name__ == "__main__":
    print(render_markdown(SAMPLE_MD))