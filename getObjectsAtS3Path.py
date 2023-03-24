def getObjectsAtS3Path(str: s3_path):
    '''Takes in an S3 path (must be a string) and returns of a list of objects at that S3 path. Currently meant for use in a Databricks environment'''
    s3_objects = []
    
    for x in dbutils.fs.ls(s3_path):
        #the dbutils.fs.ls returns a a list of FileGet object which is a tuple of length 4 where the first element is the object name
        s3_objects.append(x[0])
        
    return s3_objects