class WBuilder:
    def __init__(self):
        self.html_before = ''
        self.html_after = ''
        self.html_full = ''

    def _parse_inline(self, dct: dict) -> str:
        inline_args = ''
        for key, value in dct.items():
            inline_args += f'{key}: {value}; '
        return inline_args[:-1]

    def _parse_args(self, args: dict) -> str:
        element_args = ''
        for key, value in args.items():
            if key == 'style' and isinstance(value, dict):
                value = self._parse_inline(value)
            if key == 'class' and isinstance(value, list):
                value = ' '.join(value)

            element_args += f' {key}="{value}"'
        return element_args

    def add(self, element: str, inner: str, before: bool=False, after: bool=False, between: bool=True, **kwargs):
        element_html = f'<{element}{self._parse_args(kwargs)}>{inner}</{element}>\n{" "*12}'

        if before:
            self.html_before += element_html
        if after:
            self.html_after += element_html
        if between:
            return element_html

        self.html_full = self.html_before + element_html + self.html_after
        return self.html_full

    def add_navbar(self)

    def build(self, *args):
        return self.html_before + '\n'.join(args) + self.html_after

    def __str__(self):
        return self.html_full

if __name__ == '__main__':
    b = WBuilder()
    print(b._parse_args({'style': {'color': 'red', 'font-size': 'larger'}, 'class': ['example', 'container']}))
