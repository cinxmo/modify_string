from pydantic import BaseModel


class StringInputRequest(BaseModel):
    string_to_cut: str


class StringOutputResponse(BaseModel):
    return_string: str
