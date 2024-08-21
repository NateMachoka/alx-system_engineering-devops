# Define the holberton user
user { 'holberton':
  ensure     => present,
  managehome => true,
  shell      => '/bin/bash',
}

# Ensure the holberton user has sudo privileges without requiring a password
# Create a sudoers file for the holberton user
file { '/etc/sudoers.d/holberton':
  ensure  => file,
  content => "holberton ALL=(ALL) NOPASSWD:ALL\n",
  mode    => '0440',
}
