import os
import sys
import argparse
import subprocess

from ruamel.yaml import YAML
from pathlib import Path
from shutil import rmtree

def main( argv = sys.argv ):
    """Clean an iGUIDE project directory by keeping only terminal files."""

    try:
        conda_prefix = os.environ.get("CONDA_PREFIX")
    except (KeyError, IndexError):
        raise SystemExit(
            "Could not determine Conda prefix. Activate your iGUIDE "
            "environment and try this command again.")

    usage_str = "iguide %(prog)s <path/to/config.file> <options>"

    description_str = (
        "Clean an iGUIDE project givin a configuration file. This command will "
        "remove all but terminal files from a project directory.")
    
    parser = argparse.ArgumentParser(
        prog = "clean", 
        usage = usage_str,
        description = description_str
    )

    parser.add_argument(
        "config", 
        help = ("name of config file (%(default)s)"),
        metavar = "CONFIG_FILE"
    )
    
    parser.add_argument(
        "-q", "--quiet", 
        action="store_true",
        help = "Will not print messages."
    )

    parser.add_argument(
        "--remove_proj", 
        action="store_true",
        help = "Removes the entire project analysis directory. This will delete everything."
    )

    parser.add_argument(
        "-i", "--iguide_dir", 
        default = os.getenv("IGUIDE_DIR"),
        help = "Path to iGUIDE installation."
    )
    

    # The remaining args will not be used
    args, remaining = parser.parse_known_args(argv)
    
    # iGUIDE directory
    iguide_directory = Path(args.iguide_dir)
    
    if not iguide_directory.exists():
        sys.stderr.write(
            "Error: could not find iGUIDE directory '{}'\n".format(
                args.iguide_dir))
        sys.exit(1)
    
    # Load config yaml file
    yaml = YAML(typ = 'safe')
    config = yaml.load(open(args.config, "r"))
    
    analysis_directory = iguide_directory / "analysis" / config['Run_Name']

    if not analysis_directory.exists():
        sys.stderr.write(
            "Error: could not find analysis directory '{}'\n".format(
                str(analysis_directory)))
        sys.exit(1)

    if not args.remove_proj:
        directories_to_clean = ["input_data", "logs", "processData"]
        
        files_to_clean = []
        for directory in directories_to_clean:
            directory = analysis_directory / directory
            files = os.listdir( directory )
            for file in files:
                files_to_clean = files_to_clean + [
                  os.path.join( directory, file )
                ]
          
        for file in files_to_clean:
            if Path( file ).exists():
                os.remove( file )
                if not Path( file ).exists():
                    if not args.quiet:
                      print( "  Removed:", file )
                else:
                    print( "  Could not remove:", file )
            else:
                if not args.quiet:
                      print( "  File does not exist:", file )
    else:
        rmtree( analysis_directory )
        if not args.quiet:
            print("  Removed:", analysis_directory)
