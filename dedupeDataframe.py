def dedupeDataframe(df, partition_fields, order_by_field, ascending=False):
    """A fuinction that takes in a Spark dataframe and returns a deduped version based off supplied parameters"""
    from pyspark.sql.functions import row_number, col, desc, ascending
    from pyspark.sql.window import Window
    
    if type(partition_fields) is not list:
        partition_fields = list(partition_fields)
        
    if ascending:
        windowSpec = Window.partitionBy(*partition_fields).orderBy(col(order_by_field).asc())
    else:
        windowSpec = Window.partitionBy(*partition_fields).orderBy(col(order_by_field).desc())
        
    df = df.withColumn('rank', row_number().over(windowSpec))
    df = df.filter(col('rank') == 1).drop(col('rank'))
    
    return df