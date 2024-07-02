# Ensure the nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure index file is present and contains 'Hello World!'
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx server block for the default site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure nginx is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define the nginx configuration template
file { 'nginx/default.erb':
  ensure  => present,
  content => @"
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
"@
}
