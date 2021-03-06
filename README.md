[![Documentation Status](https://readthedocs.org/projects/vicc-metakb/badge/?version=latest)](https://vicc-metakb.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/cancervariants/metakb.svg?branch=master)](https://travis-ci.org/cancervariants/metakb) [![Coverage Status](https://coveralls.io/repos/github/cancervariants/metakb/badge.svg?branch=master)](https://coveralls.io/github/cancervariants/metakb?branch=master)

# metakb

The intent of the project is to leverage the collective knowledge of the disparate existing resources of the VICC to improve the comprehensiveness of clinical interpretation of genomic variation. An ongoing goal will be to provide and improve upon standards and guidelines by which other groups with clinical interpretation data may make it accessible and visible to the public. We have released a preprint discussing our initial harmonization effort and observed disparities in the structure and content of variant interpretations.

## Getting Started

> These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

* python3

```
python3 --version
Python 3.7.1
```

### Installing

Install requirements

```
pip3 install -r requirements.txt
```

Install requirements-dev

```
pip3 install -r requirements-dev.txt
```


> TODO End with an example of getting some data out of the system or using it for a little demo

## Running the tests

### Unit tests

Explain how to run the automated tests for this system

```
python3 -m pytest
```


### Break down into end to end tests

> TODO Explain what these tests test and why

```
TODO Give an example
```

### And coding style tests

Code style is managed by [flake8](https://github.com/PyCQA/flake8) and checked prior to commit.

```
see .flake8

```

## Deployment

> TODO Add additional notes about how to deploy this on a live system

## Built With

* [pre-commit](https://pre-commit.com) - Build chain
* [dvc](https://dvc.org) - Data version control
* TODO ... add more

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Committing

We use [pre-commit](https://pre-commit.com/#usage) to run conformance tests.

This ensures:

* Check code style
* Check for added large files
* Detect AWS Credentials
* Detect Private Key

Before first commit run:

```
pre-commit install
```

### Data Version Control

We use [dvc](https://dvc.org) to run ensure reproducibility by consistently maintaining a combination of input data, configuration, and the code that was initially used to harvest and transform data.  DVC is storage agnostic [S3, Azure, GCP, SSH, SFTP, hdfs, ...].  The metakb source and processed data is maintained on an s3 bucket.

By default DVC expects your AWS CLI is already [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). DVC will be using default AWS credentials file to access S3. To override some of these settings, you could alter the options described in `dvc remote modify`. e.g. `dvc remote modify metakb profile my-profile --local`

Once setup is complete, you are ready to pulls data files to the project working space. By default, the [dvc pull](https://dvc.org/doc/commands-reference/pull) command will retrieve and link all data dependences for the current branch into the project workspace.



## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/cancervariants/metakb/tags).

## Authors

* TODO

See also the list of [contributors](https://github.com/cancervariants/metakb/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
