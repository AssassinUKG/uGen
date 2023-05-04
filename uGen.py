#!/usr/bin/env python3

# Created by: Richard Jones from defencelogic.io
# Date 04-05-2023
# Purpose: Generate name variations for use in password spraying and phishing campaigns

import argparse
import yaml

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

def email_variations(name, domain, config):
    # Split the name into first and last name
    first, last = name.split()
    
    # Get the email variations from the configuration file
    email_variations = config
    
    # Create a list of email variations using different separators and domains
    result = []
    for variation in email_variations:
        # Evaluate any expressions in the variation
        formatted_variation = eval(f'f"""{variation}"""')
        
        # Add the formatted variation to the result list
        result.append(formatted_variation.replace('{domain}', domain))
    
    return result


if __name__ == '__main__':
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description='Generate name variations')
    parser.add_argument('-n', '--name', metavar='NAME', help='The name to generate variations for')
    parser.add_argument('-c', '--config', metavar='FILE', default='name_variations.yaml',
                        help='The name variations configuration file (default: %(default)s)')
    parser.add_argument('-e', '--email-domain', metavar='DOMAIN', default='example.com',
                        help='the domain to use for the generated email addresses (default: %(default)s)')
   
    parser.add_argument('-v', '--verbose', action='store_true', help='print verbose output')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    
    # Check if args.config is supplied if not use name_variations.yaml but also check if the file exists
    try:
        with open(args.config) as f:
            pass
    except FileNotFoundError:
        print(f"ERROR: The file {args.config} does not exist")
        exit(1)

    if args.name is None:
        print(f"ERROR: The name is not specified: -n \"Richard Jones\"")
        exit(1)
    if args.name:
        try:
            f,l = args.name.split()
        except ValueError:
            print(f"ERROR: The name is not in the correct format (firstname lastname), ie: -n \"Richard Jones\"")
            exit(1)
    

    # Load the name variations configuration from the file
    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    variations = config['variations']
    email_variation = config['email_variations']
    
    # if domain is supplied then don't generate name variations
    email_supplied = False
    if args.email_domain != 'example.com':
        email_supplied = True



    # Generate the name variations for the given name
    name_variations = name_variations(args.name, variations)
    
    # Print the name variations
    if not email_supplied:
        if args.verbose:
            print(f"Generating name variations for {args.name} using configuration file {args.config}...")
        for name_variation in name_variations:
            print(name_variation)

    # Generate email variations if requested
    else:
        email_variations = email_variations(args.name, args.email_domain, email_variation)
        for email_variation in email_variations:
            print(email_variation)
        if args.verbose:
            print(f"Generating email variations for {args.name} using domain {args.email_domain}...")
