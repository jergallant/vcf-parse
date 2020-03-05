# vcf-parse
VCF parsing exercise

usage: parse_vcf.py [-h] [-o output_file] input_file

-h shows usage\
-o optional output file. If not specified, output is printed to standard out\
input_file is the input VCF file (required)

Example:
>python parse_vcf.py sample.vcf\
chr20:10019093A>G\
chr20:10026348A>G\
chr20:10026357T>C\
chr20:10030188T>A\
...

Requires Python3.6 or later


