#copyright wangjie xmuspeech
#2021.9.16
. ./cmd.sh
. ./path.sh
#prepare data for EEVAD

WAV_DIR=/tsdata/diarization/voxconverse21_duke
KALDI_DATA_DIR=data/kaldi


INSTRUCTION=prepare_data
./voxconverse_run.sh $INSTRUCTION $WAV_DIR $KALDI_DATA_DIR



