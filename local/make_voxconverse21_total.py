#!/usr/bin/env python3
# copyright wangjie xmuspeech
# This script is called by local/make_voxconverse21_total.sh, and it creates the
# necessary files for VoxConverse 2021 development directory.

import sys, os

def prepare_voxconverse21(src_dir, data_dir):
    wavscp_fi = open(data_dir + "/wav.scp" , 'w')
    utt2spk_fi = open(data_dir + "/utt2spk" , 'w')
    spk2utt_fi = open(data_dir + "/spk2utt", 'w')
    wavScp_lines = []
    utt2spk_lines = []
    spk2utt_lines = []
    for subdir, dirs, files in os.walk(src_dir):
        for file in files:
            filename = os.path.join(subdir, file)
            if filename.endswith(".wav"):
                utt = os.path.basename(filename).split(".")[0]
                wavScp_line = "{} {}\n".format(utt, filename)
                wavScp_lines.append(wavScp_line)
                utt2spk_line = "{} {}\n".format(utt, utt)
                utt2spk_lines.append(utt2spk_line)
                spk2utt_line = "{} {}\n".format(utt, utt)
                spk2utt_lines.append(spk2utt_line)
    wavscp_fi.writelines(wavScp_lines)
    utt2spk_fi.writelines(utt2spk_lines)
    spk2utt_fi.writelines(spk2utt_lines)
    wavscp_fi.close()
    utt2spk_fi.close()
    spk2utt_fi.close()
    return 0




def main():
    src_dir = sys.argv[1]
    data_dir = sys.argv[2]
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    prepare_voxconverse21(src_dir, data_dir)
    # elif dataset == "dev":
    #     prepare_voxconverse21_dev(src_dir, data_dir)
    # elif dataset == "eval":
    #     prepare_voxconverse21_eval(src_dir, data_dir)
    return 0

if __name__=="__main__":
    main()
