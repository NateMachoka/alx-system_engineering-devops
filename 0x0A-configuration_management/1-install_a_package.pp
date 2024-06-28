# Install flask using pip3

package { 'python3-pip':
  ensure => installed,
}

python::pip { 'Flask':
  ensure  => '2.1.0',
  pip_provider => 'pip3',
}
