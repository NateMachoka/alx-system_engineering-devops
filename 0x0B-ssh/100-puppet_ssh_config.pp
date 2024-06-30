file { '/home/ubuntu/.ssh/config':
  ensure => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile\s+',
  ensure => 'present',
}

file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  PasswordAuthentication no',
  match => '^\s*PasswordAuthentication\s+',
  ensure => 'present',
}

file_line { 'Start Host block':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'Host myserver',
  match => '^Host\s+myserver',
  ensure => 'present',
}

file_line { 'Declare HostName':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  HostName 18.209.178.235',
  match => '^\s*HostName\s+',
  ensure => 'present',
}

file_line { 'Declare User':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  User ubuntu',
  match => '^\s*User\s+',
  ensure => 'present',
}
