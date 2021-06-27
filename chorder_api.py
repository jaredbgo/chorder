from fastapi import FastAPI, Query, Response, status
from chorder import key_finder


chorder = FastAPI(title="Chorder", description="Retrieve the chords of a key")

@chorder.get("/chorder/")
async def read_item(response: Response, root_note: str=Query(..., description="root note of the scale e.g. 'C'"), 
                    scale: str=Query(default="major")):

    ret_dict = {}
    try:

        init_dict = key_finder(root_note, scale)
        init_key = list(init_dict.keys())[0]

        chord_list = init_dict[init_key]

        ret_key = init_key.replace("Chords of ", "")

        ret_dict[ret_key] = chord_list

        ret_dict['success'] = True

    except Exception as e:
        ret_dict['success'] = False
        ret_dict['error'] = str(e)
        response.status_code = status.HTTP_400_BAD_REQUEST


    return ret_dict