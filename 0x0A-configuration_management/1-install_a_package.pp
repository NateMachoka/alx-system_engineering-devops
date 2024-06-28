# Install flask using pip3

package { 'flask':
  ensure   => '2.1.0',
  pip_provider => pip3,
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  pip_provider => pip3,
}