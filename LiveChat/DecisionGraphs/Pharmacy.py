from Graph import GraphTraversal
def create_PharmacyGraph():
    graph =     {
    "1":{
        "content":"Welcome!",
        "blockLLM":"False",
        "buttons":[],
        "next":[2],

    },
    "3":{
        "content":"How can we help you today? Feel free to ask us anything regarding your prescriptions",
        "blockLLM":"False",
        "buttons":[{
            "content":"order a prescription", "next":[]
        }, "check a fill", ""],
        "next":[2],
    },
    "4":{
        "content":"Certainly I can help you with that, please give me your date of birth",
        "blockLLM":"True",
        "buttons":[],
        "next":[2],
    },
    "5":{
        "content":"Welcome!",
        "blockLLM":"False",
        "buttons":[],
        "next":[2],
    },
    "6":{
        "content":"Welcome!",
        "blockLLM":"False",
        "buttons":[],
        "next":[2],
    },
    "7":{
        "content":"Welcome!",
        "blockLLM":"False",
        "buttons":[],
        "next":[2],
    }
    }
    g = {"node1":
        {
           "id":"",

        }
    }
