class ApplicationHelper:
    @staticmethod
    def full_title(page_title=''):
        """ページごとの完全なタイトルを返します。
        """
        base_title = 'Ruby on Rails Tutorial Sample App'
        if not page_title:
            return base_title
        else:
            return f'{page_title} | {base_title}'
