# find out why Apache is returning a 500 error, fix it and then automate it using Puppet

exec { 'wordpress-fix-php':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/usr/bin/:/bin/',
}

