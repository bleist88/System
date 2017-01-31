# Git Repository Help

## A Git Repository on a Server

The web info on this, while potentially more correct, is not helpful in the
slightest.  It seems to be absolutely backwards to *ACTUALLY* making a
repository on a server work.

The general pattern for making a repository from scratch:

    1. Making a "bare" repository on the server. ( the master? )
    2. Cloning the "bare" to a "working" directory on the server
       or on a remote computer.
    3. The *bare* revieves pushes and the working directories pull.

### 1. Making the "bare":

As far as I can tell, the "bare" is just the central hub for version control.
This directory doesnt contain any files that are part of the actual repository,
or at least not in any familiar form.  All changes to the repository dont get
made here, they just get pushed here.

```terminal

user@server$	mkdir Example.git
user@server$	cd Example.git
user@server$	git init --bare --shared
```

### 2. Cloning the "bare":

Somewhere else on the server or a remote computer, the actual repository may be cloned and operated on.

```terminal

user@server$	git clone <path/to/>Example.git
user@server$	cd Example/
user@server$	< make files / play with shit / just hit "clear; ls;" a bunch >
user@server$    git push

user@elsewhere$    git pull
```
