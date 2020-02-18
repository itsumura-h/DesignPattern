from enum import Enum
from datetime import date

class ScreeningStatusV1(Enum):
    """採用選考ステータス
    """
    not_applied = '未応募'
    interview = '面接'


class ScreeningV1:
    """採用選考クラス
    """
    # 採用選考ID
    __screening_id: int
    # 応募日
    __apply_date: date
    # 採用選考ステータス
    __status: ScreeningStatusV1
    # 応募者メールアドレス
    __applicant_email_address: str

class ScreeningStepResult(Enum):
    """面接結果
    """
    pass

class InterviewV1:
    """面接クラス
    """
    # 面接ID
    __interview_id: int
    # 採用選考ID
    __screening_id: int
    # 選考日
    __screening_date: date
    # 面接次数
    __interview_number: int
    # 面接結果
    __screening_step_result: ScreeningStepResult
    # 採用担当者ID
    __recruter_id: int