#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import subprocess as subproc
import re
import os
import time

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
    time.sleep(2)
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    imglst, err = proc.communicate()

    lines = (imglst.decode('ascii')).splitlines()
    if debug:
        print("Images: \n{}\n".format("\n".join(lines)))

    for line in lines: 
        contid = chk_img(imgname, tag, line, debug)

        if contid:
            print("Container built: {}".format(contid))
            return contid

    print("No image build: \n{}".format("\n".join(lines)))
    exit(1)

    return 1

def run_proc(imgname, tag, passwd, port, debug=False):
    ''' run docker image '''

    cmd = 'echo ' + passwd + '| sudo -S docker run -d -p ' + port + ' ' + \
            ' --name ' + imgname + tag + ' ' + imgname + ':' + tag
    if debug:
        print("Run process cmd: \n {}".format(cmd))
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
    time.sleep(2)
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)
    
    proclst, err = proc.communicate()

    lines = (proclst.decode('ascii')).splitlines()
    
    if debug:
        print("Processes: \n{}\n".format("\n".join(lines)))

    for line in lines:
        contid = chk_proc(imgname, tag, line, debug)

        if contid:
            print("Process run: {}".format(contid))
            return contid    

    print("No process run: \n{}".format("\n".join(lines)))
    exit(1)

    return 1

def run_redis_proc(imgname, tag, passwd, debug=False):
    ''' run Redis container '''
    cmd = 'echo ' + passwd + ' | sudo docker run -d --name redis ' \
        + imgname + tag

    proc = subproc.PIPE(cmd, shell=True, stdin=subproc.PIPE,
        stdout-subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)

    output, err = proc.communicate()
    if debug:
        if output:
            print("Run Redis proc: {}".format(output.decode('utf-8')))
        if err:
            print("Run Redis error: {}".format(err.decode('utf-8')))

    return 0

def redis_cont(passwd, debug = False):
    ''' build and run Redis container 
        1. check redis container existence -> using default Redis container
        2. run redis container if not existed 
        
        Redis container: 
            imgname: redis
            tag: v3.2.0
    '''
    # define constant varibales
    imgname = 'redis'
    tag = 'v3.2.0'

    # check redis process
    cmd = 'echo ' = passwd + ' | sudo docker ps -a '
    if debug:
        print("Display process - Redis: \n {}".format(cmd))
    proc = subproc.Popen(cmd, shell=True, stdin=subproc.PIPE, 
        stdout=subproc.PIPE, stderr=subproc.STDOUT, close_fds=True)

    output, err = proc.communicate()
    if debug:
        if output: 
            print("Redis Cont ID: {}".format(output.decode('utf-8')))
        if err:
            print("Error msg - Redis: {}".format(err.decode('utf-8')))

    # check existence of Redis container
    lines = (proc.decode('utf-8')).splitlines()

    pattern = r'^([0-9|a-f]+)\s+' + imgname + ':' + tag

    for line in lines:
        contid = re.findall(pattern, line)

        # existence checking
        if contid:
            print("\nExisted Container ID: {}".format(contid))
            return 0

    return 0


def build(debug = False):
    passwd = 'beatrice'
    imgname = 'dockerapp'
    tag = 'v0.3'
    port = '5000:5000'

    redis_cont(debug)

    del_dockerporc(imgname, tag, passwd, debug)
    del_dockerimg(imgname, tag, passwd, debug)
    build_img(imgname, tag, passwd, debug)
    run_proc(imgname, tag, passwd, port, debug)


    return 0

if __name__ == '__main__':
    # build()
    build(debug = True)
