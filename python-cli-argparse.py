import argparse

def main():
    """ Process arguments """
    # comand-line arguments
    parser = argparse.ArgumentParser(prog='cli.py',
                                     usage='python %(prog)s [-h]')
    parser.add_argument("action", choices=['action1'],
                        help="action to perform; {action1}: action1 description")
    parser.add_argument("--download", action='store_true',
                        help="Download PDB sequences")
    parser.add_argument("-d", "--directory",
                        help="Output directory, defaults to current date: year_month_day/")
    parser.add_argument("-value", default=1e-20, type=float,
                        help="float value")
    parser.add_argument("-i", "--input",
                        help="Input file")
    parser.add_argument("-o", "--output",
                        help="Output file")
    parser.add_argument("-e", "--exclude", nargs="+", default=[],
                        help="exclude multiple files")
    parser.add_argument('-v', '--verbose', action='store_true')
    
    # Validate arguments
    args = parser.parse_args()
    
    # Dispatch jobs
    # .. vervosity
    verbose = args.verbose
    # .. Today
    today = datetime.date.today()
    today_string = "%4d_%02d_%02d"%(today.year, today.month, today.day)
    # .. Work Directory
    if args.directory is None:
        output_dir = os.path.join( os.getcwd(), today_string )
    else:
        output_dir = os.path.abspath(args.directory)
    if not os.path.isdir(output_dir): os.makedirs(output_dir)
    # .. Generate BLAST DB
    if args.action == 'action1':
        output_file = args.output if args.output else os.path.join(output_dir,"output_name.out")
        # do action1

if __name__ == '__main__':
    main()
    
