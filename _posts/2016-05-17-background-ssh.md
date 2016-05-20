---
title: Running SSH port forwarding in the background
excerpt: |+
    Jupyter Notebook is essential for interacting with data. Even better,
    you can run it on a server (that has your data, more processors, more RAM, ...)
    but access it from anywhere. By default, Jupyter only serves data to `localhost`
    on port 8888.

    Instead of opening your notebook server to the world, you can set up port forwarding
    over ssh to piggy-back on the security it provides. In this post,
    we'll set up a persistent port-forwarding connection in the background.
---

[Jupyter Notebook] is essential for interacting with data. Even better,
you can run it on a server (that has your data, more processors, more RAM, ...)
but access it from anywhere. By default, Jupyter only serves data to `localhost`
on port 8888. Instead of opening your server to the world, you can set up port forwarding
over ssh to piggy-back on the security it provides.

    ssh -L 8888:localhost:8888 user@hostname

<div class="alert alert-danger" role="alert">
  <strong>Warning:</strong> If you share the remote host with any other users,
  they can get to any port! You have to set up TLS on your 
  notebook server as well.
</div>

This either (a) wastes a whole terminal to keep your ssh session alive
or (b) causes you to use the ssh session, forget that it's sustaining
your notebook, close the connection, and watch in horror as your notebook
loses all connection to its kernel. The solution is to open your connection
in the background. You can tell ssh to run
in the background with `-fNT`

    ssh -fNT -L 8888:localhost:8888 user@hostname

Now you can't ever *close* the connection! SSH can set up a "master" socket
and query it from a "control" socket.

    ssh -M -S my-socket-name -fNT -L 8888:localhost:8888 user@hostname
    ssh -S my-socket-name -O check user@hostname
    >> Master running (pid=3517) 
    ssh -S my-socket-name -O exit user@hostname
    >> Exit request sent. 

### Set up config

For a particular host, you can tell it to always use a pre-named control
socket with no ill effects. Edit `.ssh/config`:

    Host hostname
        HostName hostname
        ControlPath ~/.ssh/hostname.ctl

You can make things really easy with a couple of aliases. Edit `.bashrc`:

    alias hname-up='ssh -fNTML 8888:localhost:8888 hostname'
    alias hname-status='ssh -TO check hostname'
    alias hname-down='ssh -TO exit hostname'

### Reference

`-f`
:   Run in the background before command execution.

`-N`
:   Don't execute any commands

`-T`
:   Disable pseudo-tty allocation. I don't know what this means.

`-S socketname`
:   Use a control socket with name `socketname`

`-M`
:   Put control socket in master mode

`-O` `check`, `exit`
:   Control command

### Sources

- [Stack Overflow]
- Discussion on this [gist]
- `man ssh`

[Jupyter Notebook]: http://jupyter.org/
[Stack Overflow]: http://stackoverflow.com/questions/2241063/bash-script-to-setup-a-temporary-ssh-tunnel
[Gist]: https://gist.github.com/scy/6781836
