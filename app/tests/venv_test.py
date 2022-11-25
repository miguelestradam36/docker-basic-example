import pytest

def test_dependencies(virtualenv):
    """
    Test modules into python virtual environment
    """
    import yaml
    import os

    # Repeated values
    filepath = "../src/config/defaults.yaml"
    fullpath = os.path.join(os.path.dirname(__file__), filepath)

    with open(fullpath, 'r') as file:
        global yaml_config
        yaml_config = yaml.safe_load(file)
    
    installed_packages = virtualenv.installed_packages()
    
    for module in yaml_config["python"]["global"]["modules"]["standard"]:
        assert module['install'] or module['import'] in installed_packages

    for module in yaml_config["python"]["services"]["modules"]:
        assert module['install'] or module['import'] in installed_packages

    for module in yaml_config["python"]["global"]["modules"]["test"]:
        assert module['install'] or module['import'] in installed_packages