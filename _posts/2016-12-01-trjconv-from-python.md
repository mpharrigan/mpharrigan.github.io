---
title: Use Gromacs Utilities from Python
excerpt: |+
    Gromacs has some neat command-line programs to interact with MD trajectories. A lot of them prompt for additional input when you're running them. I'll show you how to use Python's `subprocess` module to deal with this.
---

## Subprocess

In Python, you can call an external program with the `subprocess` module. For example

    import subprocess
    subprocess.check_call(['convert', 'image.jpg', 'image.png'])
{: .language-python}

will call ImageMagik's `convert` utility. Note that the arguments need to be given as a list of strings (not one big string). You might be tempted to do

    "convert image.jpg image.png".split()
{: .language-python}

to make it feel more natural. This might cause problems. You should use [shlex.split](https://docs.python.org/3/library/shlex.html#shlex.split) instead. 

## Gromacs `trjconv`

Gromacs trjconv is useful. Despite being one of the primary maintainers of [mdtraj](http://mdtraj.org), I still use it sometimes (blasphemy!). An example run looks like this:

    $ gmx trjconv -f XTCs/Traj0/nug2-0.xtc -s nug2.pdb -o newtraj.xtc
    GROMACS:    gmx trjconv, VERSION 5.0.7

    [stuff removed here]

    Library dir:  /home/harrigan/opt/gromacs/share/gromacs/top
    Command line:
      gmx trjconv -f XTCs/Traj0/nug2-0.xtc -s nug2.pdb -o newtraj.xtc

      Will write xtc: Compressed trajectory (portable xdr format): xtc
      Select group for output
      Group     0 (         System) has   846 elements
      Group     1 (        Protein) has   846 elements
      Group     2 (      Protein-H) has   435 elements
      Group     3 (        C-alpha) has    56 elements
      Group     4 (       Backbone) has   168 elements
      Group     5 (      MainChain) has   225 elements
      Group     6 (   MainChain+Cb) has   278 elements
      Group     7 (    MainChain+H) has   283 elements
      Group     8 (      SideChain) has   563 elements
      Group     9 (    SideChain-H) has   210 elements
      Select a group:

You have to input numbers sometimes! We can do this with `subprocess`

## Communicate

You have to get down and dirty with the subprocess module to handle this. Instead of simply calling `call` (or its variants), we will open a process object and mess with it. The full details are in the [python docs](https://docs.python.org/3/library/subprocess.html).

    traj_fn = 'in.xtc'
    out_fn = 'out.xtc'
    top_fn = 'nug2.pdb'
    p = subprocess.Popen(['gmx', 'trjconv', '-center',
                          '-f', traj_fn, '-s', top_fn,
                          '-o', out_fn],
                         stdin=subprocess.PIPE)
    p.communicate(b'1\n0\n') # Center on protein, output everything
    p.wait()
{: .language-python}

We send a byte string (`b"this is a string of bytes"`) to the process after it has been started with the `communicate()` method. We give `subprocess` advanced notice that we're going to do this by telling it to read `stdin=subprocess.PIPE`. You can send whatever input you want here. Note that we use `\n` to send "enter". You can use multiple calls to `communicate` if you want:

    p = Popen(...)
    p.communicate('1\n')
    p.communicate('0\n')
    p.wait()
{: .language-python}


Now you can script gromacs like a champ!
