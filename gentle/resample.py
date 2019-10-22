import os
import subprocess

from contextlib import contextmanager

FFMPEG = '/home/wenhao/.linuxbrew/bin/ffmpeg'


def resample(infile, outfile, offset = None, duration = None):
    if not os.path.isfile(infile):
        raise IOError("Not a file: %s" % infile)

    '''
    Use FFMPEG to convert a media file to a wav file sampled at 8K
    '''
    if offset is None:
        offset = ''
    else:
        offset = ' -ss ' + str(offset)
    if duration is None:
        duration = ''
    else:
        duration = ' -t ' + str(duration)

    cmd = FFMPEG + ' -loglevel quiet -y ' + offset + ' -i ' + infile + duration + ' -ac 1 -ar 8000 -acodec ' \
                                                                                  'pcm_s16le ' + outfile
    return subprocess.call(cmd, shell = True)


@contextmanager
def resampled(infile, outfile, offset = None, duration = None):
    if resample(infile, outfile, offset, duration) != 0:
        raise RuntimeError("Unable to resample/encode '%s'" % infile)
    yield outfile
