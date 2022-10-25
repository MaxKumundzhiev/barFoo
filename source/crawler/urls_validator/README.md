# URL Validator
URL Validator module stands for validating whether a particular string represents a valid web application.

# URL Validator Usage
```python
url={urlToValidate}

validator = UrlValidator()
valid_url = validator.validate(url)  # False | validUrlAddress

if valid_url is not False:
    ...
```
