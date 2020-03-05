import argparse
import sys

# Simple argument parser to specify vcf input file and (optional) output file
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help = "the vcf file to be parsed")
parser.add_argument("-o", "--output", help = "optional output file")
args = parser.parse_args()

in_file = args.input_file
out_file = args.output if args.output else None

# Wrap the file open commands in try-except to avoid throwing stack-traces at the user
try:
    input_fo = open(args.input_file, 'r')
except FileNotFoundError:
    sys.exit("Sorry, could not find a file named %s" % args.input_file)

if out_file:
    try:
        output_fo = open(out_file, 'w')
    except Exception as e:
        sys.exit("Could not open the specified output file for writing.\nError message: %s" %e)

# Map the fixed, mandatory column names to positions
# These column positions are fixed by the spec, so we shouldn't need to build this dynamically from the header row
column_map = {
    "#CHROM": 0,
    "POS": 1,
    "ID": 2,
    "REF": 3,
    "ALT": 4,
    "QUAL": 5,
    "FILTER": 6,
    "INFO": 7
}

# Parse the file line by line
while True:
    line = input_fo.readline()
    if not line:
        # We have reached EOF. (Empty lines will be '\n')
        break

    # clean up the newline at the end of the line
    line = line.rstrip('\n')

    # Skip metadata lines
    if line.startswith('##'):
        continue
    
    # Skip the header line
    if line.startswith('#CHROM'):
        continue

    # Split data line into list using tab delimiter
    entries = line.split('\t')
    # Select the relevant values from the row
    chrom = entries[column_map['#CHROM']]
    pos = entries[column_map['POS']]
    ref = entries[column_map['REF']]
    alt = entries[column_map['ALT']]
    
    # Make the output string
    line_out = f'chr{chrom}:{pos}{ref}>{alt}'
    
    # Write output to file, or print out if no output file is specified
    if out_file:
        output_fo.write(line_out)
        output_fo.write('\n')
    else:
        print(line_out)

# Close those file handles
input_fo.close()
if out_file:
    output_fo.close()
    