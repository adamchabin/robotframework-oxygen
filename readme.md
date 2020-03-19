# OXYGEN 

Oxygen is a [Robot Framework](https://robotframework.org/) library that empowers the user to convert the results of any testing framework to the [Robot Framework's test results](https://robotframework.org/robotframework/2.1.2/RobotFrameworkUserGuide.html#created-outputs). 

Oxygen has built-in parsers for 3 testing frameworks. 

1. [JUnit](https://en.wikipedia.org/wiki/JUnit) - unit testing framework for Java.
2. [Gatling](https://en.wikipedia.org/wiki/Gatling_(software)) - load and performance testing framework.
3. [Zed Attack Proxy(ZAP)](https://www.zaproxy.org/) - web security tool. 

Additionally, users can add your own parsers for any other testing framework tools to get the results in the Robot Framework's test results. 

# Table of Contents
1. [Using Oxygen](#getting-started)
    1. [Prerequisites]()
    2. [Installation]()
    3. [Sample test case]()
    4. [Using from command line]()
2. [Developing Oxygen]()
    1. [Prerequisites]()
    2. [Installation in development environment]()
    3. [Running sample tests in development environment]()
3. [License]()
4. [Acknowledgements]()

## Using Oxygen

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Oxygen requires `Python 3.0` or above to be installed in the environment the Oxygen tool is to be deployed. 

Check the Python version on the command line:
```
python --version
```

Upgrade the python version if python version is less than `Python 3.0`. Follow the link for [python3](https://realpython.com/installing-python/) installation.

##### IMPORTANT!! --  Oxygen requires the git repository to be cloned to a directory where there is no 'spaces' in the directory path.

### Installation

### Sample test case

### Using from command line

## Developing Oxygen

### Prerequisites

Refer the prerequisites in the "Using Oxygen" section.

### Installation in development environment

Clone the Oxygen repository to the enviromnent where you want to the run the tool. Make sure that there are no 'spaces' in the directory path where the oxygen-core folder is cloned into.

Clone oxygen-core directory from the command line using:

```
git clone https://git.dev.eficode.io/scm/ox/oxygen-core.git
```
Change directory into the oxygen-core directory from command line:
```
cd oxygen-core
```
Oxygen requires a set of dependencies to be installed. Dependencies are listed in the requirements.txt file. 

Install the dependencies for Oxygen from the command line. 

```
pip install -r requirements.txt
```

### Running sample tests in development environment

Few sample tests has been written in the directory `test`in the oxgyen-core directory. To run the sample tests run the invoke command on the command line.

```
invoke atest
```
```
invoke utest
```
```
invoke test
```
To learn more about `invoke`, refer documentation of [python library](http://www.pyinvoke.org/).

## License

Details of project licensing can be found in the LICENSE file in the project repository.

## Acknowledgments

Oxygen tool  was developed by Eficode Oy as part of [Testomat project](https://www.testomatproject.eu/) with funding by [Business Finland](https://www.businessfinland.fi/).