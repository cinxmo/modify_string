from fastapi import FastAPI
from app import schemas, utils

app = FastAPI()


@app.post("/test/")
async def create_string_cut(string_to_cut: schemas.StringInputRequest):
    """
    :param string_to_cut: input string to cut
    :return: JSON response
    """
    output_str = utils.retrieve_n_letter(string_to_cut.string_to_cut)
    return schemas.StringOutputResponse(return_string=output_str)
