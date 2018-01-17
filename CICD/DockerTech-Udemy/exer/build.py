#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import subprocess as subproc
import re
import os

def chk_proc(imgname, tag, line, debug = False):
    ''' check the existing pf process and return container ID if existed'''
    pattern = r'^([0-9|a-f]+)\s+' + imgname + ':' + tag
    contid = re.findall(pattern, line)

    if debug and contid:
        print("\nContainer ID: {}".format(contid))

    return contid

def del_dockerporc(imgname, tag, passwd, debug = False):
    ''' retrieve docker process list and check existence,
        if existed, remoeve the process with container id'''
    cmd = 'echo ' + passwd + '| sudo -S docker ps -a'
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    proclst, err = proc.communicate()

    if debug: 
        print("\n\nlist of process: \n{}".format(proclst.decode('ascii')))
        if err:
            print("stderr: {}".format(err.decode('ascii')))

    lines = (proclst.decode('ascii')).splitlines()
    
    for line in lines:
        contid = chk_proc(imgname, tag, line, debug)

        ''' remove continer'''
        if contid:
            cmd = 'echo ' + passwd + '| sudo -S docker rm ' + contid[0]
            proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
                stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
            
            if debug:
                output = (proc.stdout.read()).decode('ascii')
                print("Output of docker rm: {}".format(output))

    return 0

def chk_img(imgname, tag, line, debug = False):
    ''' check existence of given process, if existed retunr container ID'''
    pattern = r'^' + imgname + '\s+' + tag + '\s+([0-9|a-f]+).*'

    contid = re.findall(pattern, line)

    if debug and contid:
        print("\nContainer ID: {}".format(contid))

    return contid

def del_dockerimg(imgname, tag, passwd, debug = False):
    ''' retrieve images list and check existence,
        if existed, remoeve the process with container id'''
    cmd = 'echo ' + passwd + '| sudo -S docker images'
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    imglst, err = proc.communicate()

    if debug: 
        print("\nlist of images: \n{}".format(imglst.decode('ascii')))
        if err:
            print("stderr: {}".format(err.decode('ascii')))

    lines = (imglst.decode('ascii')).splitlines()
    
    for line in lines:
        contid = chk_img(imgname, tag, line, debug);

        if contid:
            cmd = 'echo ' + passwd + '| sudo -S docker rmi ' + contid[0]
            proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
                stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
            
            if debug:
                output = (proc.stdout.read()).decode('ascii')
                print("Output of docker rm: {}".format(output))

    return 0

def build_img(imgname, tag, passwd, debug = False):
    ''' build docker image with provide image name and tag'''

    workdir = os.path.dirname(os.path.realpath(__file__))

    cmd = 'echo ' + passwd + '| sudo -S docker build -t ' + imgname + ':' + \
        tag + ' ' + workdir 
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)

    output, err = proc.communicate()
    if debug:
        if output: 
            print("Cont ID: {}".format(output.decode('ascii')))
        if err:
            print("Error msg: {}".format(err.decode('ascii')))

    ''' verify the built image'''
    cmd = 'echo ' + passwd + '| sudo -S docker images'
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    imglst, err = proc.communicate()

    lines = (imglst.decode('ascii')).splitlines()

    for line in lines: 
        contid = chk_img(imgname, tag, line, debug)

        if contid:
            print("Container built: {}".format(contid))
            return contid

    print("No image build: \n{}".format(lines))
    exit(1)

    return 1

def run_proc(imgname, tag, passwd, port, debug=False):
    ''' run docker image '''

    cmd = 'echo ' + passwd + '| sudo -S docker run -d -p ' + port + ' ' + imgname + ':' + tag + ' .'
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)

    output, err = proc.communicate()
    if debug:
        if output: 
            print("Cont ID: {}".format(output.decode('ascii')))
        if err:
            print("Error msg: {}".format(err.decode('ascii')))

    ''' verify running process'''
    cmd = 'echo ' + passwd + '| sudo -S docker ps -a'
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    proclst, err = proc.communicate()

    lines = (proclst.decode('ascii')).splitlines()
    
    for line in lines:
        contid = chk_proc(imgname, tag, line, debug)

        if contid:
            print("Process run: {}".format(contid))
            return contid    

    print("No process run: \n{}".format(lines))
    exit(1)

    return 1


def build(debug = False):
    passwd = 'beatrice'
    imgname = 'dockerapp'
    tag = 'v0.2'
    port = '5000:5000'

    del_dockerporc(imgname, tag, passwd, debug)
    del_dockerimg(imgname, tag, passwd, debug)
    build_img(imgname, tag, passwd, debug)
    run_proc(imgname, tag, passwd, port, debug)


    return 0

if __name__ == '__main__':
    build()
    # build(debug = True)
