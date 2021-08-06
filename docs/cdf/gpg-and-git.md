
## Configuring git to use your GPG key and credentials

Open a new Ubuntu 20.04 Terminal Window, paste the command beginning with gpg below to list your gpg key, which will be used to sign your commits.

``` bash
me@my-pc:~$ gpg --list-secret-keys --keyid-format LONG
/home/devops/.gnupg/pubring.kbx
-------------------------------
sec   rsa4096/A9E3031D40E7A31F 2021-06-03 [SC]
     71859D719307C206B6936735A9E3031D40E7A31F
uid                 [ultimate] ~Your Name~ (enter comment here) ~your email address~
ssb   rsa4096/B8239EB7C4286DAB 2021-06-03 [E]
me@my-pc:~$
```

We will be using the key displayed to configure git, here using the example key above `A9E3031D40E7A31F` taken from the 4th line:
`sec rsa4096/A9E3031D40E7A31F 2021-06-03 [SC]`

Enter the following commands, substituting your _name_, _email address_, and _gpg signingkey._

``` bash
me@my-pc:~$ git config --global gpg.program gpg
me@my-pc:~$ git config --global commit.gpgsign true
me@my-pc:~$ git config --global user.signingkey A9E3031D40E7A31F
me@my-pc:~$ git config --global user.name "~Your Name~"
me@my-pc:~$ git config --global user.email ~your email address~
me@my-pc:~$
```

Now verify that the config is correct, by typing _cat ~/.gitconfig:_ You should see something similar to below, but with your credentials.

``` bash
me@my-pc:~$ cat ~/.gitconfig
[gpg]
       program = gpg
[commit]
       gpgsign = true
[user]
       signingkey = A9E3031D40E7A31F
       name = ~Your Name~
       email = ~your email address~
me@my-pc:~$
```
