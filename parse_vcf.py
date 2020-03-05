import argparse
import sys

# Simple argument parser to specify vcf input file and (optional) output file
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help = "the vcf file to be parsed")
parser.add_argument("-o", "--output", help = "optional output file")
args = parser.parse_args()

try:
    input_file_handle = open(args.input_file, 'r')
except FileNotFoundError:
    sys.exit("Sorry, could not find a file name %s" % args.input_file)

# Parse the file line by line

# skip metadata lines
# may wish to make use of the headear line
# process each data line

file_handle.close()
    