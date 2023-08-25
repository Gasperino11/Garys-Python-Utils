def createDDLfromDataframe(df, tablename):
    """A function that creates a SQL DDL from a Dataframe"""
    ddl = f"CREATE OR REPLACE TABLE {tableName} (\n"
    
    for column, dtype in df.dtypes:
        ddl += f"\t{column} {dtype},\n"
    
    ddl = ddl[:-2]
    
    return ddl