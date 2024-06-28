# Install flask using pip3

package { 'python3-pip':
  ensure => installed,
}

python::pip { 'Flask':
  ensure  => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}