#increase user limit for opening files
exec { 'holberton-hard-limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'holberton-soft-limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf',
  path  => '/usr/local/bin/:/bin/',
}
