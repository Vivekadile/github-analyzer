from pydantic import BaseModel 
class AnalyzeRequest(BaseModel):

    github_url:str

class QuestionRequest(BaseModel):
    question:str

class AnswerResponse(BaseModel):
    answer:str
