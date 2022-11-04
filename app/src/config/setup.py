class SetUpExecuter():

    os = __import__('os')
    sys = __import__('sys')
    logging = __import__('logging')

    filepath = "\\config\\defaults.yaml"
    prefix = "python -m"

    def __init__(self):
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='installments.log')
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.logging = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.logging.addHandler(fileHandler)

    def install_all(self)->None:
        self.read_defaults()
        self.global_installs()
        self.install_test_modules()
        self.install_services()
        self.install_api_modules()

    def global_installs(self)->None:
        self.log.info("Checking in to global installations...")

        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.prefix, module["install"]))
        
        self.log.info("\n")

    def install_services(self)->None:
        self.log.info("Checking in to api-connection and app installations...")

        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.prefix, module["install"]))
        
        self.log.info("\n")

    def install_api_modules(self)->None:
        self.log.info("Checking in to services installation...")

        for module in self.yaml_config["python"]["global"]["modules"]["api-connection"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.prefix, module["install"]))
        
        self.log.info("\n")

    def install_test_modules(self)->None:
        self.log.info("Checking in to services installation...")

        import sys

        module_ = 'pytest-virtualenv'

        if module_ in sys.modules:
            self.log.info("Checking {} module into venv".format(module_))
        else:
            self.log.info("Installing {} module into venv".format(module_))
            self.os.system("{} pip install {}".format(self.prefix, module_))    

        for module in self.yaml_config["python"]["global"]["modules"]["test"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.prefix, module["install"]))
        
        self.log.info("\n")

    def read_defaults(self)->None:

        fullpath = self.os.path.join(self.os.path.dirname(__file__), self.filepath)

        try:
            self.log.info("Checking {} module into venv".format("yaml"))
            assert __import__("yaml")
        except ImportError as error:
            self.log.info("Installing {} module into venv".format("PyYaml"))
            self.os.system("{} pip install {}".format(self.prefix,"PyYaml"))
        finally:
            yaml = __import__("yaml")
        
        self.log.info("Reading configuration variables on YAML...")
        with open(fullpath, 'r') as file:
            self.yaml_config = yaml.safe_load(file)
        
        self.log.info("\n")