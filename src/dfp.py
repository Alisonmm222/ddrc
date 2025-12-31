
"""import sys
sys.path.append("notebooks/dfp.py")
from notebooks import dfp

processed_df = dfp.get_processed_df(pd.read_csv("data/raw/Tabelle Migration.csv", sep =";"))
"""

class DataFramePipeline:
    def __init__(self, df):
        df.dropna(inplace=True)
        self.df = df
        self.processed_df = df.copy()

    def reset_processing(self):
        self.processed_df = self.df.copy()
        return self


    def filter_rows(self, columnname, values):
        self.processed_df = self.processed_df.loc[self.processed_df[columnname].isin(values)]
        return self


    def drop_columns(self, columnnames):
        self.processed_df.columns = self.processed_df.columns.str.strip()
        self.processed_df = self.processed_df.drop(
        columns=columnnames,
        errors="ignore"
    )
        return self

    def rename_columns(self,
                       columns_dict):
        self.processed_df = self.processed_df.rename(columns=columns_dict)
        return self

    def convert_column_type(self, col_name, new_type):
        self.processed_df[col_name] = self.processed_df[col_name].astype(new_type)
        return self

    def convert_numeric_data_to_float(self):
        cols_to_conv = [col for col in self.processed_df.columns if col != "Gemeinde"]
        for c in cols_to_conv:
            self.processed_df[c] = self.processed_df[c].str.replace(",", ".").astype("float")
        return self

    def get_processed_df(self):
        return self.processed_df


def get_processed_df(df):
    dfp = DataFramePipeline(df)
    processed_df = ((dfp
     .filter_rows("Raumeinheit", ["Kelheim", "Straubing-Bogen", "Straubing", "Freyung-Grafenau", "Passau, Stadt", "Regen", "Deggendorf",
                                  "Dingolfing-Landau", "Landshut, Stadt", "Rottal-Inn", "Passau"])
     .drop_columns(["Aggregat","Kennziffer"])
     .rename_columns({"Raumeinheit": "Gemeinde"}))
     .convert_column_type("Gemeinde", "string")
    .convert_numeric_data_to_float()
     .get_processed_df())
    return processed_df