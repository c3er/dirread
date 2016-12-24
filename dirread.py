#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jinja2


def main():
    with open("template.html", encoding="utf8") as f:
        content = f.read()
    template = jinja2.Template(content)
    rendered = template.render(
        path="Test path",
        message="Hello, world!"
    )
    print(rendered)


if __name__ == '__main__':
    main()
