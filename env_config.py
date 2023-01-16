from dotenv import dotenv_values

class EnvConfig:
    def __init__(self, env_file=".env"):
        self.config = dotenv_values(env_file)

    def get_s3bucket(self):
        if "S3_BUCKET" not in self.config:
            raise ValueError("S3_BUCKET not set in the environment")
        return self.config["S3_BUCKET"]

    def get_s3object(self, search_object:str=None):
        if "S3_OBJECT" not in self.config:
            raise ValueError("S3_OBJECT not set in the environment")

        s3_object_list = list(self.config["S3_OBJECT"].split(","))
        if search_object is None:
            return s3_object_list
        else:
            try:
                index = s3_object_list.index(search_object)
                return s3_object_list[index]
            except ValueError:
                print(f"{search_object} not found in S3_OBJECT list")

    def get_accesskey(self):
        if "IAM_ACCESS_KEY" not in self.config:
            raise ValueError("IAM_ACCESS_KEY not set in the environment")
        return self.config["IAM_ACCESS_KEY"]

    def get_secretkey(self):
        if "IAM_SECRET_KEY" not in self.config:
            raise ValueError("IAM_SECRET_KEY not set in the environment")
        return self.config["IAM_SECRET_KEY"]

    def get_iamid(self):
        if "IAM_ID" not in self.config:
            raise ValueError("IAM_ID not set in the environment")
        return self.config["IAM_ID"]

    def get_iamuser(self):
        if "IAM_USER" not in self.config:
            raise ValueError("IAM_USER not set in the environment")
        return self.config["IAM_USER"]
        
    def get_dburl(self):
        if "DB_URL" not in self.config:
            raise ValueError("DB_URL not set in the environment")
        return self.config["DB_URL"]

    def get_dbuser(self):
        if "DB_USER" not in self.config:
            raise ValueError("DB_USER not set in the environment")
        return self.config["DB_USER"]

    def get_dburl(self):
        if "DB_NAME" not in self.config:
            raise ValueError("DB_NAME not set in the environment")
        return self.config["DB_NAME"]

    def get_dbpassword(self):
        if "DB_PASSWORD" not in self.config:
            raise ValueError("DB_PASSWORD not set in the environment")
        return self.config["DB_PASSWORD"]