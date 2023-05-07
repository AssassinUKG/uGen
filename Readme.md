# uGen.py

## Menu
- [Information](https://github.com/AssassinUKG/uGen/Readme.md#information)
- [Usage](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#usage)
- [Screenshots](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#screenshots)
- [Installation](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#installation)
- [Configuration File](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#configuration-file)
- [Output Example](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#output)
- [Help](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#help)
- [Changelog](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#changelog)
- [Licence](https://github.com/AssassinUKG/uGen/edit/master/Readme.md#licence)

### Information 
uGen.py name managler is a Python command-line tool for generating variations of names and email addresses based on a configuration file. It provides a flexible way to generate a wide range of name and email variations, which can be useful for creating usernames or email addresses for a large number of users.

### Usage
To use the uGen.py name managler, simply run the main.py script and provide the name to generate variations for using the -n or --name option. You can also specify a different configuration file using the -c or --config option, and a different email domain using the -e or --email-domain option. 
> You can also supply a suffix for emails only. 

Example usage:

```python
$ python3 uGen.py -n "John Smith"
$ python3 uGen.py -n list_of_usernames.txt
$ python3 uGen.py -n "John Smith" -e example.org
$ python3 uGen.py -n "John Smith" -c name_variations.yaml -e example.org
$ python3 uGen.py -n "John Smith" -e example.org -s 1992
```
>This will generate name and email variations for the name "John Smith" using the variations specified in the variations.yaml configuration file and the email domain example.org.

### Screenshots

![image](https://user-images.githubusercontent.com/5285547/236194670-dcfd8f1a-0109-4c9b-a2f8-86444f55c275.png)

## Installation
To install uGen.py name managler, simply clone or download the repository and install the required packages using pip:

```bash
git clone https://github.com/AssassinUKG/uGen.git
cd uGen
pip install -r requirements.txt
```

## Configuration file
The configuration file is a YAML file that contains the variations to be used in generating name and email variations. The variations section contains the name variations, and the email_variations section contains the email variations.  
You can add or remove variations to suit your needs.

Example configuration file:

```yaml
variations:
  - ["{first}", "{last}"]             # First Last
  - ["{first}", ".", "{last}"]        # First.Last
  - ["{first[0]}", ".", "{last}"]     # F.Last
  - ["{first}", "{last}"]             # FirstLast
  - ["{first[0]}", "{last}"]          # FLast
  - ["{first.lower()}", ".", "{last.lower()}"]   # first.last
  - ["{first[0].lower()}", ".", "{last.lower()}"] # f.last
  - ["{first}", "_", "{last}"]        # First_Last
  - ["{first[0]}", "_", "{last}"]     # F_Last
  - ["{first}", "-", "{last}"]        # First-Last
  - ["{first[0]}", "-", "{last}"]     # F-Last
  - ["{first}", "_", "{last[0]}"]     # First_L

email_variations:
  - '{first}.{last}@{domain}'
  - '{first[0]}.{last}@{domain}'
  - '{first}{last}@{domain}'
  - '{first[0]}{last}@{domain}'
  - '{last}.{first}@{domain}'
  - '{last}{first}@{domain}'
```

### Output
Normal
```
JohnSmith
John.Smith
J.Smith
JohnSmith
JSmith
john.smith
j.smith
John_Smith
J_Smith
John-Smith
J-Smith
John_S
J_S
John-S
J-S
john_smith
j_smith
john-smith
j-smith
Smith,John
smith,john
Smith,J.
smith,j.
Smith-John
smith-john
Smith_John
smith_john
S.John
S.J
S_John
S_J
S-John
SJohn
Sjohn
```
Email
```
John.Smith@somedom.com
J.Smith@somedom.com
S.John@somedom.com
JohnSmith@somedom.com
JSmith@somedom.com
Smith.John@somedom.com
SmithJohn@somedom.com
John@somedom.com
Smith@somedom.com
```
Email & suffix
```
Smith1992@example.org
JSmith1992@example.org
```

### Help

```sh
usage: uGen.py [-h] [-n NAME] [-c FILE] [-e DOMAIN] [-s SUFFIX] [-v]

Generate name variations

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  The name to generate variations for
  -c FILE, --config FILE
                        The name variations configuration file (default: name_variations.yaml)
  -e DOMAIN, --email-domain DOMAIN
                        the domain to use for the generated email addresses (default: example.com)
  -s SUFFIX, --suffix SUFFIX
                        The suffix to add to the generated email addresses (default: )
  -v, --verbose         print verbose output
```

### Changelog

07/05/2023 - Added ability to use username of file of usernames

### License
uGen.py name managler is licensed under the MIT License. See the LICENSE file for details.
