# make changes to our configuration file.
file { 'ssh.config':
  ensure  => 'present',
  path    => '/.ssh/ssh_config',
  content => @("SSHCONF")
    Host *
       IdentityFile ~/.ssh/school
       PasswordAuthentication no
    | SSHCONF
}
