import pandas as pd

data = {
    'PostMention': [
        "[1, 2, 3]",
        "{'key': 'value'}",
        "(4, 5, 6)"
    ]
}

df_post = pd.DataFrame(data)
