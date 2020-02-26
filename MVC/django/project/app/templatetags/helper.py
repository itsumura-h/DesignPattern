from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムタグとして登録する
@register.simple_tag
def full_title(page_title=''):
    base_title = 'Ruby on Rails Tutorial Sample App'
    if not page_title:
        return base_title
    else:
        return f'{page_title} | {base_title}'
