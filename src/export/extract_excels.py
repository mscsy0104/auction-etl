import pandas as pd

def extrat_excel(data):
    df = pd.DataFrame(data)
    from datetime import datetime
    dtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath = f"./results/seoul_calendar_{dtime}.xlsx"
    df.to_excel(filepath)