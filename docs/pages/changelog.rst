.. _changelog:

.. contents::
   :depth: 2

ChangeLog 
========================

**v0.9.8 (March 8th, 2019)**

* iGUIDE can now support non-Cas9 nucleases as well!
  + Implemented nuclease profiles into configs
  + Updated assimilation, evaluation, and reporting scripts
* Added default resources to allow simpler HPC processing.

**v0.9.7 (March 6th, 2019)**

* Hotfix to workflow.
* Changed 'setup' subcommand to python script based rather than snakemake.
* Changed file organization.

**v0.9.6 (March 5th, 2019)**

* Introduced process workflow steps: assimilate and evaluate
  + Assimilate aligned data and compare with targeting sequences
    + Core data object that can be combined across runs / projects
  + Evaluated data incorporates reference data and statistical models
    + A staple data object for reports and can be constructed from multiple runs
* Included new subcommands 'eval' and modified 'report'
  + report from either config(s) or eval dataset
* Cleaned up file structure
* Updated documentation in code and docs.
* Implemented accuracy and retention checks with simulation dataset.
* Updated simulation dataset with larger set to test analysis.

**v0.9.5 (February 19th, 2019)**

* Updated demultiplexing to be more efficient and better HPC compatible.
* Added RefSeq Extended* reference gene sets
  + 'ext' includes curated, predicted, and other RefSeq sets
  + 'ext.nomodel' includes only curated and other RefSeq sets
* Incorporated resource allocation for job dependent memory consumption
  + Works great with HPC to specify memory requirements
* Streamlined input for report generation by only requiring config(s)

**v0.9.4 (January 30th, 2019)**

* Updated 'report' utility and formating
  + custom templates now accepted
  + included as subcommand, check with 'iguide report -h'
  + pdf and html options report 'nicely' even when printed from either
* Updated build to v0.9.2 to support new formating in report
* Builds are constructed from spec files rather than yaml requirements
* Included the 'clean' subcommand to reduce size of processed projects
  + after cleaning a project, only terminal data files will remain

**v0.9.3 (January 11th, 2019)**

* Added 'list_samples' subcommand to list samples within a project.
* Caught a few bugs and worked them out for smoother processing and reports.

**v0.9.2 (January 7th, 2019)**

* Modified test dataset to run tests quicker and implemented CirclCI checking.

**v0.9.1 (January 6th, 2019)**

* Fixed problematic install for first time conda installers.

**v0.9.0 (January 4th, 2019)**

* Initial release.
* Supports setup and analysis of GUIDE-seq and iGUIDE experiments.
* Documentation on [ReadTheDocs.io](https://iguide.readthedocs.io/en/latest/index.html).
