from fastapi import FastAPI
from chorder import key_finder


chorder = FastAPI()

@chorder.get("/chorder/")
async def read_item(root_note,scale='major'):

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


    return ret_dict