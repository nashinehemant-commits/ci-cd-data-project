from notebooks.data_pipeline import clean_data
import pandas as pd


def test_clean_data():
    data = {'amount': ['10', '20', None]}
    df = pd.DataFrame(data)

    cleaned_df = clean_data(df)

    assert cleaned_df.shape[0] == 2
    assert cleaned_df['amount'].dtype == float