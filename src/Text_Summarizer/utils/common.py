import  os
from box.exceptions import BoxValueError
import yaml
from Text_Summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox # For yaml file (see trials.ipynb) To acces value using keys
from pathlib import Path
from typing import Any


@ensure_annotations #   
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if the yaml file is empty
        e: empty yaml file
    
    Returns:
        ConfigBox: a ConfigBox type object
    
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaed successfully.")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.

    Args:
        path_to_directories (list): a list of path of  directories
        ignore_log (bool, optional): ignore if multiple  dirs  is to be created. Defaults  to False

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully.")




@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path (str): path of the file
    
    Returns:
        str: size of the file in KB
    
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

