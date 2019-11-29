import re

class ScreeningApplicationServiceV1:
    """アプリケーションサービス
    """

    @staticmethod
    def is_invalid_format_email_address(email:str):
        if email == None:
            return False

        CONST_EMAIL_REGEX = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
        return re.match(CONST_EMAIL_REGEX, email)
        

    def start_from_pre_interview(self, applicant_email_address:str):
        # 入力チェック
        if applicant_email_address is None or \
                self.is_invalid_format_email_address(applicant_email_address):
            raise Exception('メールアドレスが正しくありません')