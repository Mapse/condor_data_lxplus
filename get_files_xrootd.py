import subprocess, os, re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def generate_path(dataset,  crab_folder, n_folders):

    cmds = [ 
    f'xrdfs k8s-redir.ultralight.org:1094 ls -u /store/group/uerj/mabarros/Charmonium/{dataset}_AOD/{crab_folder}/{i:04}/' for i in range(n_folders)
    ]
    #print(cmds)

    cat = ""
    out_file = dataset + "_path.txt"
    for i in cmds:
        os.system(f"{i} > {i.split('/')[-2]}")
        cat += f" {i.split('/')[-2]}"

    os.system(f"cat {cat} > {out_file}")
    os.system(f"rm -rf {cat}")
    file_list = open(out_file, 'r').readlines()

    for idx, f in enumerate(file_list):
        file_list[idx] = re.sub('transfer-\d*', 'xrootd-redir', f)
    
    list(set(file_list))
    file_list.sort(key=natural_keys)

    final_list = []
    for i in file_list:
        if i not in final_list:
            final_list.append(i)

    transfer_counter = 1
    for idx, f in enumerate(final_list):
        final_list[idx] = re.sub('xrootd-redir', 'transfer-' + str(transfer_counter), f)
        transfer_counter += 1
        if transfer_counter > 10:
            transfer_counter = 1

    with open(out_file, 'w') as f:
        for i in final_list:
            f.write(i)

if __name__ == '__main__':


    dataset = [# 2016
               'CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1',
               'CharmoniumRun2016C_21Feb2020_UL2016_HIPM-v1', 
               'CharmoniumRun2016D_21Feb2020_UL2016_HIPM-v1',
               'CharmoniumRun2016E_21Feb2020_UL2016_HIPM-v1',
               'CharmoniumRun2016F_21Feb2020_UL2016_HIPM-v1',
               'CharmoniumRun2016F_21Feb2020_UL2016-v1',
               'CharmoniumRun2016G_21Feb2020_UL2016-v1',
               'CharmoniumRun2016H_21Feb2020_UL2016-v1',
               # 2017
               'CharmoniumRun2017B_09Aug2019_UL2017-v1',
               'CharmoniumRun2017C_09Aug2019_UL2017-v1', 
               'CharmoniumRun2017D_09Aug2019_UL2017-v1', 
               'CharmoniumRun2017E_09Aug2019_UL2017-v1',
               'CharmoniumRun2017F_09Aug2019_UL2017-v1',
               # 2018
               'CharmoniumRun2018A_12Nov2019_UL2018_rsb-v1', 
               'CharmoniumRun2018B_12Nov2019_UL2018-v1',
               'CharmoniumRun2018C_12Nov2019_UL2018_rsb_v2-v2',
               'CharmoniumRun2018D_12Nov2019_UL2018-v1'
               ]
    
    crab_folder = [#2016
                   '221009_034842', 
                   '221009_021601', 
                   '221009_034847', 
                   '221009_034852',
                   '221009_034858',
                   '221009_034903', 
                   '221009_034908', 
                   '221009_040921',       
                   # 2017
                   '220902_015029',
                   '220828_034208', 
                   '220828_034213', 
                   '220828_131648',
                   '220828_034223',
                   # 2018
                   '220828_034746',
                   '220828_034751', 
                   '220816_015519', 
                   '220829_145333',]
    
    # Number of folders in the production (number of folders: 0000, 0001, 0002...)
    n_folders_2016 = [4, 2, 3, 3, 2, 1, 5, 6]
    n_folders_2017 = [2, 7, 3, 7, 9]
    n_folders_2018 = [8, 5, 4, 10]

    n_folders = n_folders_2016 + n_folders_2017 + n_folders_2018 

    """ dataset = ['CharmoniumRun2016B_21Feb2020_ver2_UL2016_HIPM-v1',]
    crab_folder = ['221009_034842', ]
    n_folders = [4,] """
    
    for d, c, n in zip(dataset, crab_folder, n_folders):
        print(f"Processing: {d}...")
        generate_path(d, c, n)     
###########