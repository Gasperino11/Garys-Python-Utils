def computDataframeCardinality(df, id_fields, num_sample_rows=10):
    """A function to report on the cardinality of ID fields in a Spark dataframe; made for use in Databricks"""
    from pyspark.sql.functions import col, desc
    
    print("Dataframe Cardinality:")
    
    numRows = df.count()
    print(f"-- Number of rows: {numRows}")
    
    for field in id_fields:
        numIds = df.select(col(field)).distinct().count()
        print(f"-- Number of Unique {field}'s: {numIds}")
        
    primaryKey = col(id_fields[0])
    
    print(f"Here is a sample of {num_sample_rows} rows")
    display(df.sort(desc(primaryKey)).limit(num_sample_rows))