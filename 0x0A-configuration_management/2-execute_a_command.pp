# Manifest that kills a process named killmenow
exec { 'kill':
  command => 'pkill -9 killmenow',
  path    => '/usr/bin/',
}