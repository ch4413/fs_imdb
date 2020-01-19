"""
extractors
"""

import requests
import tarfile


def download_data(target_path='./data/aclImdb_v1.tar.gz'):
    """

    :param target_path:
    :return:
    """
    url = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
    target_path = target_path
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.raw.read())
    print('Data downloaded to' + target_path)


def unzip_file(extract_path='./data/'):
    """

    :param extract_path:
    :return:
    """
    file_name = './data/aclImdb_v1.tar.gz'

    if file_name.endswith("tar.gz"):
        tar = tarfile.open(file_name, "r:gz")
        tar.extractall(extract_path)
        tar.close()
