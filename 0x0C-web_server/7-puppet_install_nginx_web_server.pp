# Ensure the nginx package is installed


package { 'nginx':
  ensure => installed,
}

# Make sure index file is present and serves 'Hello World!'
file { 'Website index file':
  ensure  => present,
  content => 'Hello World!',
  path    => '/var/www/html/index.nginx-debian.html',
  require => Package['nginx'],
}

# Ensure 404 file is present and has 'Ceci n'est pas une page'
file { 'Website 404 file':
  ensure  => present,
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page",
}

# Ensure Nginx is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}