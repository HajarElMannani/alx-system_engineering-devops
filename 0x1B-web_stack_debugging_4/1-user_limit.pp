#increase user limit for opening files
exec { 'increase holbertin hard limit':
  command => 'sed -i "/holberton hard/s/5/5000" /etc/security/limits.conf',
  path    => "/bin/"
}

exec { 'increase holbertin soft limit':
  command => 'sed -i "/holberton soft/s/4/4000" /etc/security/limits.conf',
  path  => "/bin/"
}
