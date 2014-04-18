[ -z "$PS1" ] && return

function parse_git_dirty {
  git diff --no-ext-diff --quiet --exit-code &> /dev/null || echo "*"
}

function parse_git_branch {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/(\1$(parse_git_dirty))/"
}

export CLICOLOR=1
export EDITOR='vim -f'

export PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\$(parse_git_branch)\$ "

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# path for local python packages
export PATH=$PATH:$HOME/.local/bin
# path for google appengine
export PATH=$PATH:$HOME/.google_appengine

export HEROKU_POSTGRESQL_YELLOW_URL=postgres://dmhvcxkvjfpjtq:vfKMg7t1EnPlUVoRHcEJd3ZrNW@ec2-107-22-234-129.compute-1.amazonaws.com:5432/deb8587cr71tj7
export sourHEROKU_POSTGRESQL_ROSE_URL=postgres://wtcsziuhcqiboz:JGY_P4jJEj5rSr1CJGuGXdjiFL@ec2-107-21-226-77.compute-1.amazonaws.com:5432/d6emreq6hcslgj
export HEROKU_POSTGRESQL_YELLOW_URL=postgres://dmhvcxkvjfpjtq:vfKMg7t1EnPlUVoRHcEJd3ZrNW@ec2-107-22-234-129.compute-1.amazonaws.com:5432/deb8587cr71tj7
