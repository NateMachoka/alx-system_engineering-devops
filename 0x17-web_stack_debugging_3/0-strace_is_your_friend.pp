# 0-strace_is_your_friend.pp
# This Puppet manifest ensures that the missing PHP file exists to fix the 500 Internal Server Error

file { '/var/www/html/missing_file.php':
  ensure  => file,
  content => "<?php echo 'File exists'; ?>\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
