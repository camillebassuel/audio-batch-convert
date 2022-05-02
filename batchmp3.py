import os
import sys
import pathlib
from os import listdir
from genericpath import isdir
from os.path import isfile, join
import asyncio
import ffmpeg

def exclude_ext(ext):
    def compare(fn): return os.path.splitext(fn)[1] != ext
    return compare

def include_exts(files,exts):
    results = []
    results +=  [s for s in files if s.endswith in (exts)]
    return results


def decode_audio(in_filename, out_filename, input_kwargs, output_wargs):
  
    try:
        out, err = (ffmpeg
            .input(in_filename, **input_kwargs)
            .output(filename=out_filename,**output_wargs)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return out
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        # sys.exit(1)

def getAllFiles(pathin):
        return [f for f in listdir(pathin) if isfile(join(pathin, f))]

def convert(pathin, pathout):
    exts = ['.mp3','.m4a','.mp4','.flac','.wav']
    onlyfiles = getAllFiles(pathin)
    print(len(onlyfiles))
    files = [x for x in onlyfiles if  x.endswith(tuple(exts))]
    print(len(files))

    input_kwargs = {}
    output_kwargs = {}
    # expg = 'compand=attacks=0:points=-45/-15|-27/-9|0/-7|20/-3:gain=3'
    # bands = (
    #     'equalizer=f=440:width_type=o:width=2:g=5',
    #     'equalizer=f=1000:width_type=h:width=200:g=-10'
    # )
    # eq = ",".join(bands)
    
    # input_kwargs['filter_complex'] = expg
    output_kwargs['format']='mp3'
    output_kwargs['b:a'] = '320k'

    for file in files:
        input_file = pathlib.Path(pathin, file)
        if os.path.exists(input_file):
            nakedname = os.path.splitext(file)[0]
            output_file = pathlib.Path(pathout, nakedname + '.mp3')
            print(input_file)
            print(nakedname)
            decode_audio(input_file,output_file,input_kwargs,output_kwargs)

