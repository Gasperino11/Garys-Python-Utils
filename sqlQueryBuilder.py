def sqlQueryBuilder(table: str, database: str = None, fields: list = ["*"], conditionals: list = [], joins: dict = {}):
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

    #add joins if applicable
    if len(joins) > 0:
        for join in joins.keys():
            if database is not None:
                join_str = f"{join['how'].upper()} JOIN {database}.{join['name']} ON {join['conditions']}"
            else:
                join_str = f"{join['how'].upper()} JOIN {join['name']} ON {join['conditions']}"
    
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