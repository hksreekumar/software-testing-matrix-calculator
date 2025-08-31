# SURESOFT Workshop | Introduction Software Testing | Matrix Calculator Example
This is the base project for implementing tests and therefore for training purposes only.

## Usage

```bash
cd <PROJECT_DIR>
py -m pip install -r requirements.txt
py main.py --help
```

## Testing
### Unit testing with PyTest

<strong>Unit testing</strong>
```bash
cd <PROJECT_DIR>
py -m pytest test/unit_tests
```

<strong>Unit testing with coverage</strong>
```bash
cd <PROJECT_DIR>
py -m coverage run --source=./source -m pytest test/unit_tests
py -m coverage report -m 
```

### Acceptance testing with PyTest

<strong>Acceptance testing</strong>
```bash
cd <PROJECT_DIR>
py -m pytest test/acceptance_tests
```

<strong>Acceptance testing with coverage</strong>
```bash
cd <PROJECT_DIR>
py -m coverage run --source=./source -m pytest test/acceptance_tests
py -m coverage report -m 
```

### Code quality tests with PyLint

PyLint configurations are available in `.pylintrc`
```bash
cd <PROJECT_DIR>
py -m pylint ./source
```

## License
All rights reserved by SURESOFT, TU Braunschweig.