#!/usr/bin/env python3

# Created by: Richard Jones from defencelogic.io
# Date 04-05-2023
# Purpose: Generate name variations for use in password spraying and phishing campaigns

# Updated: 07-04-2023
# Purpose: Added ability to read file of names or one name from command line

import argparse
import yaml
import os

def name_variations(name, variations):
    # needed variable holders
    first, last = name.split()
    # Create a list of variations using different separators and capitalization
    result = []
    for variation in variations:
        if isinstance(variation, list):
            # If the variation is a list, join the elements with an empty string
            formatted_variation = ''.join(variation)
        else:
            # If the variation is a string, use it as is
            formatted_variation = variation
        
        # Evaluate any expressions in the variation
        formatted_variation = eval(f'f"""{formatted_variation}"""')
        
        # Add the formatted variation to the result list
        result.append(formatted_variation)
    
    return result

def email_variations(name, domain, config, suffix):
    # Split the name into first and last name
    first, last = name.split()
    
    # Get the email variations from the configuration file
    email_variations_config = config
    
    # Create a list of email variations using different separators and domains
    result = []
    for variation in email_variations_config:
        # Evaluate any expressions in the variation
        formatted_variation = eval(f'f"""{variation}"""')
        
        # Add the suffix before the domain name, if specified
        if suffix:
            formatted_variation = formatted_variation.replace('{suffix}', suffix)
        else:
            formatted_variation = formatted_variation.replace('{suffix}', '')
        
        # Add the formatted variation to the result list
        result.append(formatted_variation.replace('{domain}', domain))
    
    return result





if __name__ == '__main__':
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description='Generate name variations')
    parser.add_argument('-n', '--name', metavar='NAME', help='The name or file of names to generate variations for. (Format per line: firstname lastname)')
    parser.add_argument('-c', '--config', metavar='FILE', default='name_variations.yaml',
                        help='The name variations configuration file (default: %(default)s)')
    parser.add_argument('-e', '--email-domain', metavar='DOMAIN', default='example.com',
                        help='the domain to use for the generated email addresses (default: %(default)s)')
    parser.add_argument('-s', '--suffix', metavar='SUFFIX', default='',
                        help='The suffix to add to the generated email addresses (default: %(default)s)')
    parser.add_argument('-v', '--verbose', action='store_true', help='print verbose output')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    
    # Check if args.config is supplied if not use name_variations.yaml but also check if the file exists
    try:
        with open(args.config) as f:
            pass
    except FileNotFoundError:
        print(f"[!] The file {args.config} does not exist")
        exit(1)

    if args.verbose:
        banner = r"""
         ________                                 
 __ __  /  _____/  ____   ____      ______ ___.__.
|  |  \/   \  ____/ __ \ /    \     \____ <   |  |
|  |  /\    \_\  \  ___/|   |  \    |  |_> >___  |
|____/  \______  /\___  >___|  / /\ |   __// ____|
               \/     \/     \/  \/ |__|   \/     
"""
        print(f"\033[36m{banner}\033[0m")
        print("uGen.py - Generate name variations for use in password spraying and phishing campaigns")
        print("Created by: Richard Jones from defencelogic.io, on 04-05-2023")
        print("Updated: 07-04-2023") 

    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    variations = config['variations']
    email_variations_config = config['email_variations']
    
    # check if email domain is supplied
    email_supplied = args.email_domain != 'example.com'
    
    # read names from file or use the given name
    if os.path.isfile(args.name):
        with open(args.name) as f:
            names = [line.strip() for line in f]
    else:
        names = [args.name]
        
        # generate email variations if requested
    if email_supplied:
        for name in names:
            email_vars = email_variations(name, args.email_domain, email_variations_config, args.suffix)
            if args.verbose:
                print(f"[+] Generating email variations for {name} using domain {args.email_domain}...")
            for email_variation in email_vars:
                print(email_variation)
    else:
        for name in names:
            if not name:
                print("[!] The name is not specified: -n \"John Smith\"")
                exit(1)
            try:
                first, last = name.split()
            except ValueError:
                print("[!] The name is not in the correct format (firstname lastname), ie: -n \"John Smith\"")
                exit(1)
            name_vars = name_variations(name, variations)
            if args.verbose:
                print(f"[+] Generating name variations for {name} using configuration file {args.config}...")
            for name_variation in name_vars:
                print(name_variation)