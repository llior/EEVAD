#!/bin/bash
#copyright wangjie xmuspeech
#2021/9/16

. ./path.sh
. ./cmd.sh
cmd="run.pl"
set -e
#models hyperparameter
source ./config/pipeline_conf.sh

INSTRUCTION=$1
WAV_DIR=$2
KALDI_DATA_DIR=$3

if [ $# != 3 ]; then
	echo "$# wrong number of input parameters"
	exit 1
fi

if [[ $INSTRUCTION = "prepare_data" ]]; then
	#prepare kaldi data
	for SET in TRAIN DEV EVAL;do
		./local/make_voxconverse21_total.py $WAV_DIR/$SET $KALDI_DATA_DIR/$SET
	done
	
	
	
fi
