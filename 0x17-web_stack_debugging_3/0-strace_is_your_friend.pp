# This Puppet manifest ensures that the missing PHP file exists to fix
# the 500 Internal Server Error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}