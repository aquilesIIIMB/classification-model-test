# input-data-definition (DON'T REMOVE THIS COMMENT)
project_id = 'ml-framework-maas'
input_files_queries = ['input_data.sql']
valid_test_rate = [0, 0.2]
output_tables = ["model_test_iris.train_x", "model_test_iris.test_x", "model_test_iris.train_y", "model_test_iris.test_y"]

# input-data-ingestion (DON'T REMOVE THIS COMMENT)
import bigframes.pandas as bf
from sklearn.model_selection import train_test_split
from typing import List

# Auxiliar functions
def modify_query_file(input_name: str, replacements: dict={}, path='../scripts/queries/'):
    """
    Modifies file in place with a dictionary of string replacements
    """
    with open(path+input_name, 'r') as file :
        filedata = file.read()
    if replacements:
        for key, value in replacements.items():
            filedata = filedata.replace(key, value)
    return filedata

# Main function
def input_data_ingestion(
    project_id: str,
    valid_test_rate: List[float],
    location: str='us-central1',
    secret_path: List[str]=None,
    input_files_queries: List[str]=None,
    input_files_storage_uri: List[str]=None,
    test_mode: bool=False,
    labels: List[str]=None,
):
    bf.options.bigquery.location = "us"  # Dataset is in 'us' not 'us-central1'
    bf.options.bigquery.project = project_id

    input_table_query = modify_query_file(input_files_queries[0], replacements={'@PROJECT_ID': project_id}, path='queries/')
    
    df = bf.read_gbq(query_or_table=input_table_query).to_pandas()

    species_categories = {
        "versicolor": 0,
        "virginica": 1,
        "setosa": 2,
    }
    df["species"] = df["species"].map(species_categories)

    # Assign an index column name
    index_col = "index"
    df.index.name = index_col

    feature_columns = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    label_columns = df[["species"]]
    train_X, test_X, train_y, test_y = train_test_split(
        feature_columns, label_columns, test_size=valid_test_rate[1]
    )

    print("X_train size: ", train_X.size)
    print("X_test size: ", test_X.size)
    
    return (train_X, test_X, train_y, test_y)


# process (DON'T REMOVE THIS COMMENT)
from sklearn.preprocessing import StandardScaler
from typing import List
import pandas as pd

# Auxiliar functions
# ...

def feature_generation_from_input_data(
    input_data: tuple,
    project_id: str,
    location: str='us-central1',
    secret_path: List[str]=None,
    test_mode: bool=False,
    labels: List[str]=None
):
    train_X = input_data[0]
    test_X = input_data[1]
    train_y = input_data[2]
    test_y = input_data[3]
    
    # Instantiate transformer
    transformer = StandardScaler()

    # Execute transformer on Vertex (train_X is bigframes.dataframe.DataFrame, X_train is np.array)
    scaled_train_X = transformer.fit_transform(train_X)
    train_X = pd.DataFrame(scaled_train_X, index=train_X.index, columns=train_X.columns)

    # Execute transformer on Vertex (test_X is bigframes.dataframe.DataFrame, X_test is np.array)
    scaled_test_X = transformer.transform(test_X)
    train_X = pd.DataFrame(scaled_test_X, index=test_X.index, columns=test_X.columns)
    
    return (train_X, test_X, train_y, test_y)


# output-data-storing (DON'T REMOVE THIS COMMENT)

# Auxiliar functions
# ...

def feature_storing(
    feature_data: tuple,
    project_id: str,
    labels: List[str]=None,
    location: str='us-central1',
    output_tables: List[str]=None,
    output_bucket: List[str]=None,
    secret_path: List[str]=None,
    test_mode: bool=False
):
    train_X = feature_data[0]
    test_X = feature_data[1]
    train_y = feature_data[2]
    test_y = feature_data[3]
        
    train_X = train_X.reset_index(drop=True)
    train_y = train_y.reset_index(drop=True)

    test_X = test_X.reset_index(drop=True)
    test_y = test_y.reset_index(drop=True)

    train_X.to_gbq(destination_table=output_tables[0], project_id=project_id, location=location, if_exists='replace')
    test_X.to_gbq(destination_table=output_tables[1], project_id=project_id, location=location, if_exists='replace')
    train_y.to_gbq(destination_table=output_tables[2], project_id=project_id, location=location, if_exists='replace')
    test_y.to_gbq(destination_table=output_tables[3], project_id=project_id, location=location, if_exists='replace')
    
    return tuple([f'{project_id}.{table}' for table in output_tables])


# step-execution (DON'T REMOVE THIS COMMENT)

if __name__ == "__main__": 
    # Steps
    input_data = input_data_ingestion(
        project_id=project_id,
        input_files_queries=input_files_queries,
        valid_test_rate=valid_test_rate
    )

    feature_data = feature_generation_from_input_data(
        project_id=project_id,
        input_data=input_data
    )

    feature_location = feature_storing(
        project_id=project_id,
        feature_data=feature_data,
        output_tables=output_tables
    )

    print(feature_location)

