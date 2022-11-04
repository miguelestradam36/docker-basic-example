from src.config.setup import SetUpExecuter
from src.modules.aws.connector import AWSManager

if __name__ == "__main__":
    installments = SetUpExecuter()
    buff = AWSManager()
    buff.manual_secrets_log_in('<primary-key>','<secret-primary-key>')
    print('Rest is up to configuration...\n')
    # TODO: Code, feel free to use the AWSManager constructed object