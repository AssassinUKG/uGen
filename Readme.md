# uGen.py
uGen.py name managler is a Python command-line tool for generating variations of names and email addresses based on a configuration file. It provides a flexible way to generate a wide range of name and email variations, which can be useful for creating usernames or email addresses for a large number of users.

Usage
To use the uGen.py name managler, simply run the main.py script and provide the name to generate variations for using the -n or --name option. You can also specify a different configuration file using the -c or --config option, and a different email domain using the -e or --email-domain option.

Example usage:

```python
$ python main.py -n "John Smith"
$ python main.py -n "John Smith" -e example.org
$ python main.py -n "John Smith" -c name_variations.yaml -e example.org
```
>This will generate name and email variations for the name "John Smith" using the variations specified in the variations.yaml configuration file and the email domain example.org.

## Configuration file
The configuration file is a YAML file that contains the variations to be used in generating name and email variations. The variations section contains the name variations, and the email_variations section contains the email variations.  
You can add or remove variations to suit your needs.

Example configuration file:

```yaml
variations:
  - ["{first}.{last}", "{domain}"]      # First.Last@example.com
  - ["{last}.{first}", "{domain}"]      # Last.First@example.com
  - ["{first[0]}{last}", "{domain}"]    # FLast@example.com
  - ["{last}{first[0]}", "{domain}"]    # LastF@example.com
  - ["{first}{last}", "{domain}"]       # FirstLast@example.com
  - ["{last}{first}", "{domain}"]       # LastFirst@example.com
  - ["{last[0]}", ".", "{first}"]       # L.First
  - ["{last[0]}", ".", "{first[0]}"]    # L.F
  - ["{last[0]}", "_", "{first}"]       # L_First
  - ["{last[0]}", "_", "{first[0]}"]    # L_F
  - ["{last[0]}", "-", "{first}"]       # L-First
  - ["{last[0]}", "{first}"]            # lFirst
  - ["{last[0]}", "{first.lower()}"]    # lfirst

email_variations:
  - '{first}.{last}@{domain}'
  - '{first[0]}.{last}@{domain}'
  - '{first}{last}@{domain}'
  - '{first[0]}{last}@{domain}'
  - '{last}.{first}@{domain}'
  - '{last}{first}@{domain}'
```

## Output
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

## Installation
To install uGen.py name managler, simply clone or download the repository and install the required packages using pip:

```bash
git clone https://github.com/AssassinUKG/uGen.git
cd uGen
pip install -r requirements.txt
```

## License
uGen.py name managler is licensed under the MIT License. See the LICENSE file for details.
