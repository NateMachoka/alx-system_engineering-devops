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
  path    => '/usr/share/nginx/html/404.html',
  content => "Ceci n'est pas une page",
}

# Add the custom HTTP header configuration to nginx.conf
file { 'nginx.conf':
  path    => '/etc/nginx/nginx.conf',
  ensure  => present,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Template for nginx configuration
file { '/etc/nginx/templates/nginx.conf.erb':
  ensure => file,
  content => @("EOF"),
user  nginx;
worker_processes  auto;
pid        /var/run/nginx.pid;
error_log  /var/log/nginx/error.log;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80 default_server;
        server_name  _;
        root         /var/www/html;

        # Add custom HTTP header
        add_header X-Served-By $hostname;

        location / {
            try_files $uri $uri/ =404;
        }

        error_page 404 /404.html;
        location = /404.html {
            internal;
        }

        location = /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
}
| EOF
}

# Ensure Nginx is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['nginx.conf'],
}
