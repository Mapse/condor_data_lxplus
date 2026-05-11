# Processing nanoAODPlus files - Run 2 CMS data
This repository contains all codes to run the Run 2 data analysis for the associated production of J/ψ + D* with condor on lxplus.
The input files are in the nanoAODPlus format and are produced using this [repository](https://github.com/Mapse/NanoAOD). The output files
are in the _.coffea_ format.

## Files used in the processing

* quick_setup.sh
* get_files_xrootd.py
* condor.py
* jobs_template.jdl
* submit.sh
* config_files.py

The first thing to do here is to activate the conda enviroment with the files being used and use your grid credentials. These two things are
performed using:

``` quick_setup.sh ```

Now, you need to identify the path of your files. Using T2_Caltec_US as an example, the  basic command used for this is,

``` xrdfs k8s-redir.ultralight.org:1094 ls -u /store/group/uerj/mabarros ```

This is implemented in the get_files_xrootd.py script. To run it, just do:

``` python3 get_files_xrootd.py ```

You will get text files with the paths for all ultralegacy Run 2 data:
| Dataset |
|----|
| CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1 |
| CharmoniumRun2016C_21Feb2020_UL2016_HIPM-v1      |
| CharmoniumRun2016D_21Feb2020_UL2016_HIPM-v1      |
| CharmoniumRun2016E_21Feb2020_UL2016_HIPM-v1      | 
| CharmoniumRun2016F_21Feb2020_UL2016_HIPM-v1      | 
| CharmoniumRun2016F_21Feb2020_UL2016-v1           | 
| CharmoniumRun2016G_21Feb2020_UL2016-v1           | 
| CharmoniumRun2016H_21Feb2020_UL2016-v1           | 
| CharmoniumRun2017B_09Aug2019_UL2017-v1           | 
| CharmoniumRun2017C_09Aug2019_UL2017-v1           | 
| CharmoniumRun2017D_09Aug2019_UL2017-v1           | 
| CharmoniumRun2017E_09Aug2019_UL2017-v1           | 
| CharmoniumRun2017F_09Aug2019_UL2017-v1           | 
| CharmoniumRun2018A_12Nov2019_UL2018_rsb-v1       | 
| CharmoniumRun2018B_12Nov2019_UL2018-v1           | 
| CharmoniumRun2018C_12Nov2019_UL2018_rsb_v2-v2    | 
| CharmoniumRun2018D_12Nov2019_UL2018-v1           | 

Before launching the processing, it is important to guarantee that your _x509userproxy_ is at the right place. To guarantee this, edit the path on
jobs_template.jdl file:

``` x509userproxy = /afs/cern.ch/work/m/mabarros/public/CMSSW_10_6_12/src/condor/condor_data_lxplus/x509up_u128055 ```

## Running condor

To run the condor script, it is important to choose the dataset listed in the previous table. We can use CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1 as an example:

```    python3 condor.py -n=CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1 -s ```

After that, condor should run normally

> Comment: It is important follow the condor process by typing *condor_q user_name* and also look on the *output.err* files, located at CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1_logs.

Finally, when your files are ready, you just need to seed then to another repository where the other steps of the anaylsis can be performed.
