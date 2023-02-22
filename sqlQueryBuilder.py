def sqlQueryBuilder(table, database=None, fields=["*"], conditionals=[]):
    #start query
    query = "SELECT "
    
    #join fields with commas to query
    query += ",".join(fields)
    
    #start from clause
    query += " FROM "
    
    #if database is included, add that
    if database is not None:
        query += f"{database}."
    
    #add table to query
    query += f"{table}"
    
    #add conditionals
    if len(conditionals) > 0:
        query += " WHERE "
        if len(conditionals) > 1:
            query_conditions = " AND ".join(conditionals)
            query += query_conditions
        else:
            query += conditionals[0]
    
    #end query
    query += ";"
    
    #return query as string
    return query