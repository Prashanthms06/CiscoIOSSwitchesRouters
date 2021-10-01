[Main Menu](../README.md)
# Offline setup
The required softwares are already downloaded and present under downloads folder.
The following softwares are present under downloads folder:

|SofwareName|Version|
|------------|------|
|setuptools|57.0.0|
|pip|21.1.2|
|jsonschema|3.2.0|
|paramiko||

```shell
pip3 install genie
pip3 install pyats
pip3 install ttp
pip3 install scp
pip install paramiko-expect
ansible-galaxy install clay584.parse_genie

```


Install the software as per below given order:

## Installing setuptools
Run the following commands to check the version of setuptools.
```shell
easy_install --version
```
If the version of the setuptools is not too old(<41), you can skip the installation or else follow the steps below to install the setup tools:

tep 1: Download the setuptools-57.0.0.tar.gz file from the downloads folder

Step 2: Run the following command to extract
```sh
tar -zxvf setuptools-57.0.0.tar.gz
```
Step 3: Run the following commands to install  setuptools
```sh
cd setuptools-57.0.0

python3 setup.py install
```

Step 4: Once the installation is complete. Run the following command to verify the version of setuptools
```shell
easy_install --version
```

## Installing pip
If older version of pip is being used,run the following commands to upgrade the pip.

Step 1: Download the pip-21.1.2.tar.gz file from the downloads folder

Step 2: Run the following command to extract
```sh
tar -zxvf pip-21.1.2.tar.gz
```
Step 3: Run the following commands to install  pip
```sh
cd pip-21.1.2

python3 setup.py install
```

Step 4: Once the installation is complete. Run the following command to verify the version of pip
```shell
pip3 --version
```

## Installing jsonschema

Step 1: Download the jsonschema_3.2.0.tar.gz file from the downloads folder

Step 2: Step 2: Run the following command to extract
```sh
tar -zxvf jsonschema_3.2.0.tar.gz
```

Step 3: The above command will create a folder by name _jsonschema_. 
Copy the fully qualified path. (For example: /home/user/jsonschema)

Step 4: Run the following command to install the jsonschema.
**NOTE: In the below command , provide the path of jsonschema folder after the two slashes only. For
example: --find-links:file://fully_qualified_path**
```shell
 pip3 install --no-index --find-links=file:///home/user/jsonschema  jsonschema
```

Step 5: Run the following command to verify that jsonschema is installed
```shell
pip3 list | grep jsonschema
```
