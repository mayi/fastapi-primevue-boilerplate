from typing import Optional
from pydantic import BaseModel

class BaseRet(BaseModel):
    result: str
    message: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Page(BaseModel):
    page_index: int
    page_size: int
    total_result: int
    total_page: int
    offset: int
    limit: int

    def __init__(self, page_index=1, page_size=10, total_result=0, total_page=0, offset=0, limit=10) -> None:
        if page_index < 1:
            page_index = 1
        if page_size < 1:
            page_size = 10
        offset = (page_index - 1) * page_size
        limit = page_size
        if total_result < 0:
            total_result = 0
        total_page = int(total_result / page_size)
        mod = total_result % page_size
        if mod > 0:
            total_page = total_page + 1
        super().__init__(self=self, page_index=page_index, page_size=page_size,
                         total_result=total_result, total_page=total_page, offset=offset, limit=limit)
