#testing how well our web server setup featuring Nginx is doing under pressure, fix the stack so that we get to 0 failure.

exec { 'success_reqquest':
  command => 'sed -i s/15/4069/g /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}